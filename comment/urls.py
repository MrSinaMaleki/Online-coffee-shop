from django.urls import path
from .views import CommentDetailView

urlpatterns = [
# Retrieve, update, or delete a specific comment
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]