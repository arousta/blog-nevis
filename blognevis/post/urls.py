from django.urls import path

from .views import PostView


urlpatterns = [
    path("post/<uuid:pk>/", PostView.as_view(), name="post"),
]
