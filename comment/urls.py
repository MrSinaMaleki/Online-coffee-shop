from django.urls import path
from .views import CommentAPIView,CreateComment,CommentProductAPIView

urlpatterns = [
    path('comments/', CommentAPIView.as_view()),
    path('comments/<int:product_id>',CommentProductAPIView.as_view() ),
    path('', CreateComment.as_view())

]
