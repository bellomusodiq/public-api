from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ApiToken(models.Model):
    access_token = models.TextField()
    referesh_token = models.TextField()
    token_type = models.CharField(max_length=100)
    expires_in = models.BigIntegerField()


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investor_no = models.BigIntegerField()
    investor_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_ref = models.CharField(max_length=400)
    cscs_number = models.CharField(max_length=100, blank=True, null=True)
    instructions = models.CharField(max_length=400)
    trade_date_limit = models.CharField(max_length=100)
    trade_effective_date = models.CharField(max_length=100)
    trade_action = models.CharField(max_length=100)
    trade_price_limit = models.CharField(max_length=400)
    trade_unit = models.CharField(max_length=400)
    sms_pin = models.BigIntegerField(blank=True, null=True)
    stock_code = models.CharField(max_length=100)

    def __str__(self):
        return self.transaction_ref
