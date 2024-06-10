from django.urls import path

from companies import views

urlpatterns = [
    path('companies/create/', views.CompanyListCreate.as_view(), name='company-list-create'),
    path('search/', views.CompanySearchView.as_view(), name='company-search'),
    path('watchlist/', views.UserWatchlist.as_view(), name='user-watchlist'),
    path('watchlist/add/', views.AddToWatchlistView.as_view(), name='add-to-watchlist'),
]
