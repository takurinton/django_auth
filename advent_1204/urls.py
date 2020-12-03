from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('myapp.urls')), 
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token), # ここにアクセスするとJWTを発行する
]
