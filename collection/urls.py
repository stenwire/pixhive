from django.urls import path

from .views import (
    CollectionListCreateView,
    CollectionRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "", CollectionListCreateView.as_view(), name="collection-list-create"
    ),
    path(
        "<uuid:pk>/",
        CollectionRetrieveUpdateDestroyView.as_view(),
        name="collection-detail",
    ),
]
