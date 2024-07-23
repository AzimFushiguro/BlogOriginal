from django.urls import path
from .views import main_page,post_details

urlpatterns = [
    path("", main_page, name="main"),
    path("posts/<int:post_id>/", post_details, name="detail")
]
