from uuid import uuid4

from django.db import models

from users.models import Users

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company_name = models.CharField(max_length=255, null=False,blank=False)
    symbol = models.CharField(max_length=255, null=True, blank=True)
    scripcode = models.CharField(max_length=255, null=True, blank=True)
    

class Watchlist(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="user_companies")
