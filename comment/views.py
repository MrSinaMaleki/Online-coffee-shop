from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.status import HTTP_201_CREATED
from .models import Comments
from .serializers import CommentSerializer, CommentAdderSerializer
from django.db.models import Q
from rest_framework.exceptions import ValidationError

class CreateComment(APIView):
    serializer_class = CommentAdderSerializer
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

class CommentProductAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self, *args, **kwargs):
        product_id = self.kwargs['product_id']
        print(product_id)
        if not product_id:
            raise ValidationError('Product ID is required.')

        queryset = Comments.objects.filter(
            (
                    Q(child__isnull=False)
                &
                    Q(reply_comments__isnull=True)
                &
                    Q(product_id=product_id)

            ) |
            Q(reply_comments__isnull=True) & Q(product_id=product_id)

        )
        return queryset


class CommentAPIView(ListAPIView):
    serializer_class = CommentSerializer
    # No reply but a reply to a certain comment
    # Has replies but not a reply to any comment
    #Doesn't have replies and not a reply to any comment!

    queryset = Comments.objects.filter(Q(reply_comments__isnull=True)
                                       |
                                        Q(child__isnull=True)
                                        |
                                       Q(reply_comments__isnull=True, child__isnull=True))

    # def get(self, request, *args, **kwargs):
    #     all_comments = Comments.objects.filter(Q(reply_comments__isnull=True) or Q(reply_comments__isnull=True, child__isnull=True))
    #     # alone_comments = Comments.objects.filter()
    #
    #     top_level_serializer = CommentSerializer(all_comments, many=True)
    #     # alone_serializer = CommentSerializer(alone_comments, many=True)
    #
    #     return Response({
    #         'all_comments': top_level_serializer.data,
    #         # 'top_level_serializer': top_level_serializer.data,
    #         # 'alone_serializer': alone_serializer.data
    #     })