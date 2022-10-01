"""solar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include,re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from solar_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registerbusiness/', BusinessInvestorRegisterView.as_view(), name='register_business'),
    path('api/registerindividual/', IndividualInvestorRegisterView.as_view(), name='register_individual'),
    path('api/registeraffliate/', AffliateRegisterView.as_view(), name='register_affliate'),
    path('api/registersponsor/', SponsorRegisterView.as_view(), name='register_sponsor'),
    re_path(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    path('api/individualInvestorlogin/', IndividualLoginView.as_view(), name='login_individual_investor'),
    path('api/businessInvestorlogin/', BusinessInvestorLoginView.as_view(), name='login_business_investor'),
    path('api/affliatelogin/', AffliateLoginView.as_view(), name='login_affliate'),
    path('api/sponsorlogin/', SponsorLoginView.as_view(), name='login_sponsor'),
    path('api/affliaterecoverymail/',RecoverAffliatePassword.as_view(), name='affliate_password_recovery_mail'),
    path('api/businessinvestorrecoverymail/',RecoverBusinessInvestorPassword.as_view(), name='business_investor_recovery_mail'),
    path('api/businessinvestorrecoverpassword/',PasswordRecovery.as_view(), name='business_investor_password_recovery'),
    path('api/affliaterecoverpassword/',PasswordRecovery.as_view(), name='affliate_password_recovery'),
    path('api/sponsorrecoverymail/',RecoverSponsorPassword.as_view(), name='sponsor_password_recovery_mail'),
    path('api/affliates/',AllAffliatesView.as_view(), name='affliate_list'),
    path('api/salesearnings/',SaveEarninsView.as_view(), name='earnings'),
    path('api/dashboard/',AffliateDashboardView.as_view(), name='dashboard'),
    path('api/pitchproject/',PitchProjectView.as_view(), name='pitchproject'),


]
