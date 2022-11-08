from django.urls import path,include
from API import views as my_views
from . import views
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
#router.register(r'users',Register) 


router.register(r'newuser',my_views.NewUserViewSets)
urlpatterns = [
  
  #path('admin/', admin.site.urls),
  path('api/newuser/', include(router.urls)),
  

]



