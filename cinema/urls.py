from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList,
    GenreDetail,

    ActorList,
    ActorDetail,

    CinemaHallViewSet,

    MovieViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view({"get": "list", "post": "create"})
cinemahall_detail = CinemaHallViewSet.as_view(
    {"get": "retrieve",
     "put": "update",
     "delete": "destroy",
     "patch": "partial_update"}
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/",
         ActorDetail.as_view(),
         name="actor-detail"),

    path("cinema_halls/", cinemahall_list, name="cinemahall-list"),
    path("cinema_halls/<int:pk>/",
         cinemahall_detail,
         name="cinemahall-detail"),

    path("", include(router.urls)),
]

app_name = "cinema"
