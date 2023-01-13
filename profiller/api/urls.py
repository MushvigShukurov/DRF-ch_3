from django.urls import path, include
# from profiller.api import views as api_views
from profiller.api.views import ProfilViewSet
from rest_framework.routers import DefaultRouter
# profil_list = ProfilViewSet.as_view({'get':'list'})
# profil_detay = ProfilViewSet.as_view({'get':'retrieve'})

router = DefaultRouter()
router.register(r'kullanici-profilleri',ProfilViewSet)


urlpatterns = [
    # path('kullanici-profilleri/',api_views.ProfilList.as_view(),name="profiller"),
    # path('kullanici-profilleri/', profil_list, name="profiller"),
    # path('kullanici-profilleri/<int:pk>', profil_detay, name="profiller"),
    path('', include(router.urls)),
    
]

