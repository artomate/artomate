from django.urls import path
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from account.api.views import (
    registration_view,
    login,
    activate,
)
from account.api import views

app_name = 'account'

urlpatterns = [
    path('register', registration_view, name="register"),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         activate, name='activate'),

    path('login', login),
    path('kyc', views.KycView.as_view()),
    path('dashboard', views.DashboardView.as_view()),


    path('postproject', views.Projects.as_view()),
    path('home', views.AllProjects.as_view()),

    path('category', views.Category.as_view()),
    path('categorylist', views.CategoryList.as_view()),

]
