from django.contrib import admin
from django.urls import path,include
#from rest_framework.authtoken import views
from API import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/',include('API.urls')),
  #path('api-token-auth', views.obtain_auth_token)
  path('', views.homePage),
  path('login/', views.loginPage),
  path('signup/', views.signUpPage),
]