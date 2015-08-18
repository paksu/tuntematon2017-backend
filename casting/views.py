from .models import Actor, Casting
from .serializers import ActorSerializer, CastingSerializer
from rest_framework import generics


class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CastingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Casting.objects.all()
    serializer_class = CastingSerializer
