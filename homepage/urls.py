from django.urls import path
from homepage import views
app_name='homepage'

urlpatterns=[
    path('register',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
