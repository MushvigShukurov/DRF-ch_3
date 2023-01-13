from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerializer, ProfilDurumSerializer, ProfilFotoSerializer
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import OzProfiliYadaReadOnlyBrat, OzDurumuYadaReadOnlyBrat
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


class ProfilDurumViewSet(ModelViewSet):
    queryset = ProfilDurum.objects.all()
    serializer_class  = ProfilDurumSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [OzProfiliYadaReadOnlyBrat]
    permission_classes = [OzDurumuYadaReadOnlyBrat]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user.profil)

class ProfilFotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated]

    # queryset update
    def get_object(self):
        profil_nesnesi = self.request.user.profil
        return profil_nesnesi







