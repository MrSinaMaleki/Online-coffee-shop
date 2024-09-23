from rest_framework import status, generics
from .models import Comments
from .serializers import CommentsSerializer


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
