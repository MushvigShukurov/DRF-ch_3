from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerializer, ProfilDurumSerializer, ProfilFotoSerializer
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import OzProfiliYadaReadOnlyBrat, OzDurumuYadaReadOnlyBrat
from rest_framework.filters import SearchFilter
# class ProfilList(generics.ListAPIView):
#     queryset = Profil.objects.all()
#     serializer_class  = ProfilSerializer
#     permission_classes = [IsAuthenticated]



# class ProfilViewSet(ReadOnlyModelViewSet):
#     queryset = Profil.objects.all()
#     serializer_class  = ProfilSerializer
#     permission_classes = [IsAuthenticated]


class ProfilViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Profil.objects.all()
    serializer_class  = ProfilSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [OzProfiliYadaReadOnlyBrat]
    filter_backends = [SearchFilter]
    search_fields = ['sehir','bio']


class ProfilDurumViewSet(ModelViewSet):
    # queryset = ProfilDurum.objects.all()
    serializer_class  = ProfilDurumSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [OzProfiliYadaReadOnlyBrat]
    permission_classes = [OzDurumuYadaReadOnlyBrat]

    # filter
    def get_queryset(self):
        queryset = ProfilDurum.objects.all()
        username = self.request.query_params.get('username',None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset


    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.profil)

class ProfilFotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated]

    # queryset update
    def get_object(self):
        profil_nesnesi = self.request.user.profil
        return profil_nesnesi







