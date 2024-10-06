from django.urls import path
from .views import CommentAPIView,CreateComment,CommentProductAPIView,UpdateCommentReply,CommentAdminPanelView

urlpatterns = [
    path('add_comment/', CreateComment.as_view()),

    path('adding_reply/<int:comment_id>',UpdateCommentReply.as_view() ),
    path('comments/detail/<int:product_id>',CommentProductAPIView.as_view() ),
    # path('<int:commentId>', CommentAPIView.as_view())

    path('comments/admin-panel',CommentAdminPanelView.as_view() ),

]
