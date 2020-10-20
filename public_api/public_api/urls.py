"""public_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import (
    home, GetAccessToken, CreateCustomer,
    GetMarketSymbol, GetMarketData,
    GetInvestors, GetInvestorById,
    CreateListTransaction
)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', GetAccessToken.as_view()),
    path('api/login/', obtain_jwt_token),
    path('api/create-customer/', CreateCustomer.as_view()),
    path('api/market-symbols/', GetMarketSymbol.as_view()),
    path('api/market-data/', GetMarketData.as_view()),
    path('api/investors/', GetInvestors.as_view()),
    path('api/investors/<int:pk>/', GetInvestorById.as_view()),
    path('api/transactions/', CreateListTransaction.as_view()),
    path('', home)
]