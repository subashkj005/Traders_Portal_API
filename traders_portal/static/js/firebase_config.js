function firebaseOAuthSignIn() {

    document.getElementById('google-btn').addEventListener('click', function() {
        
        if (!firebase.apps.length) {
            firebase.initializeApp(firebaseConfig);
        } else {
            firebase.app(); 
        }
    
        var auth = firebase.auth();
        var provider = new firebase.auth.GoogleAuthProvider();

        auth.signInWithPopup(provider)
        .then((result) => {
            result.user.getIdToken()
            .then(token => {
                sendTokenToBackend(token);
            })
            .catch(tokenError => {
                // console.error('Error while token retrieval', tokenError);
            });
        })
        .catch((error) => {
            // console.error('Error while google signin', error.json())
        });
    });
}

function sendTokenToBackend(token) {
    fetch('/api/v1/auth/authenticate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token: token }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('OAuth Login Success:', data);
        updateUserDetails(data.data)
    })
    .catch((error) => {
        // console.error('OAuth Login Error:', error);
    });
}

function updateUserDetails(user) {
    document.getElementById('login-heading').innerHTML = `Welcome<br>${user.name}`;
    document.getElementById('login-text').innerHTML = "Login Successful";
    document.getElementById('google-sign-btn').innerHTML = `Logged in as ${user.email}`;
}

