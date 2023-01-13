from django.urls import path
from profiller.api import views as api_views

urlpatterns = [
    path('kullanici-profilleri/',api_views.ProfilList.as_view(),name="profiller"),
    
]