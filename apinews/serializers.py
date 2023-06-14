from rest_framework import serializers


class GetArticlesSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
