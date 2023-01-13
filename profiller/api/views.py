from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil
from profiller.api.serializers import ProfilSerializer
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import OzProfiliYadaReadOnlyBrat
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