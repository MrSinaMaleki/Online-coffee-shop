from rest_framework import generics, permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED
from .models import Comments
from .serializers import CommentSerializer, CommentAdderSerializer, CommentAdminPanelSerializer
from django.db.models import Q
from rest_framework.exceptions import ValidationError


class CreateComment(APIView):
    serializer_class = CommentAdderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class UpdateCommentReply(APIView):
    serializer_class = CommentAdderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, comment_id):
        try:
            parent_comment = Comments.objects.accepted().get(id=comment_id)
        except Comments.DoesNotExist:
            return Response({"error": "Parent comment does not exist."}, status=HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_reply = serializer.save(reply_comments=parent_comment)

        if hasattr(parent_comment, 'child'):
            updated_replies = CommentAdderSerializer(parent_comment.child.all(), many=True).data
        else:
            updated_replies = []

        return Response({
            "parent_comment": CommentAdderSerializer(parent_comment).data,
            "updated_replies": updated_replies
        }, status=HTTP_200_OK)


class CommentProductAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        product_id = self.kwargs['product_id']

        if not product_id:
            raise ValidationError('Product ID is required.')

        queryset = Comments.objects.accepted().filter(
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
    # Doesn't have replies and not a reply to any comment!

    queryset = Comments.objects.accepted().filter(Q(reply_comments__isnull=True)
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



'''view comment in admin panel'''


class CommentAdminPanelView(APIView):
    queryset = Comments.objects.filter(is_active=False)
    permission_classes = (permissions.IsAuthenticated, IsAdminUser)

    def get(self, request, *args, **kwargs):
        serializers = CommentAdminPanelSerializer(Comments.objects.filter(Q(is_accepted=False, is_delete=False)),
                                                  many=True)
        return Response(serializers.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        comment_id = request.data['id_comment']
        comment = Comments.objects.filter(id=comment_id).exists()
        if comment:
            comment = Comments.objects.get(id=comment_id)
            comment.is_accepted = True
            comment.save()
            return Response({"is_deleted": True}, status=HTTP_200_OK)
        return Response({"is_deleted": False}, status=HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        comment_id = request.data['id_comment']
        comment = Comments.objects.filter(id=comment_id).exists()
        if comment:
            comment = Comments.objects.get(id=comment_id)
            comment.deactivate()
            comment.make_delete()
            comment.save()
            return Response({"is_deleted": True}, status=HTTP_200_OK)
        return Response({"is_deleted": False}, status=HTTP_404_NOT_FOUND)

