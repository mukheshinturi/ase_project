from django.urls import path, re_path
from . import views
<<<<<<< HEAD

=======
>>>>>>> e2e81602d85c6bebcced2f293e90e4ff77cb60f6
urlpatterns = [
    path('',views.home,name="home"),
    path('upload/',views.model_form_upload,name='model_form_upload'),
    path('searchdata/',views.searchdata,name='searchdata')
]
