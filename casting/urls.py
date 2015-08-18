from django.conf.urls import url
from .views import ActorListAPIView, CastingListCreateAPIView

urlpatterns = [
    url(r'^/actor/', ActorListAPIView.as_view()),
    url(r'^/casting/', CastingListCreateAPIView.as_view())
]
