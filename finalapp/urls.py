from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('finalapp/form/',views.model_form_upload,name='model_form_upload')
]
