from django.contrib import admin
from .models import ApiToken, Investor, Transaction
# Register your models here.


admin.site.register(ApiToken)
admin.site.register(Investor)
admin.site.register(Transaction)
