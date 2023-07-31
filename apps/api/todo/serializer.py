from rest_framework import serializers
from apps.api.todo.models import Todo


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField(read_only=True)
    desc = serializers.CharField()
    completed = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.completed = validated_data.get("completed", instance.completed)

        return instance


