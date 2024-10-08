from rest_framework.authtoken.admin import User
from rest_framework.relations import SlugRelatedField

from comment.models import Comments
from rest_framework import serializers

from account.models import User

from product.serializers import ProductOrderSerializer


class CommentAdderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text', 'score', 'user', 'product', 'reply_comments']


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'profile_image']


class CommentSerializer(serializers.ModelSerializer):
    reply_comments = serializers.SerializerMethodField()
    user = HumanSerializer(read_only=True)

    class Meta:
        model = Comments

        fields = ['id', 'text', 'score', 'created_at','product','user','reply_comments', 'is_buyer']

        # depth = 6

    def get_reply_comments(self, obj):
        replies = obj.child.filter(reply_comments__isnull=False).filter(is_accepted=True).distinct()
        if replies.exists():
            return CommentSerializer(replies, many=True).data
        return None

    def validate_score(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('Score must be between 0 and 5.')
        return value


'''serializer admin panel comment '''


class CommentAdminPanelSerializer(CommentAdderSerializer):
    user = HumanSerializer(read_only=True)
    product = ProductOrderSerializer(read_only=True)
    reply_comments = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['text', 'score', 'user', 'product', 'reply_comments', 'id']

    def get_reply_comments(self, obj):
        if obj.reply_comments is not None:
            return CommentAdminPanelSerializer(obj.reply_comments, many=False).data
        return None
