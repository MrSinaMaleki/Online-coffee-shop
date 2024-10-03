from rest_framework.authtoken.admin import User
from rest_framework.relations import SlugRelatedField

from comment.models import Comments
from rest_framework import serializers

from account.models import Human


class CommentAdderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text', 'score', 'user', 'product', 'reply_comments']

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ['username', 'profile_image']

class CommentSerializer(serializers.ModelSerializer):
    reply_comments = serializers.SerializerMethodField()
    user = HumanSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text', 'score', 'created_at','product','user','reply_comments',]
        # depth = 6

    def get_reply_comments(self, obj):
        replies = obj.child.filter(reply_comments__isnull=False).distinct()
        if replies.exists():
            return CommentSerializer(replies, many=True).data
        return None

    def validate_score(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('Score must be between 0 and 5.')
        return value
