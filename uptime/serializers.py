from rest_framework import serializers
from uptime.models import websites
from django.contrib.auth import get_user_model

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = websites
        fields = ('website',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = (
            'id', 'username', 'email', )
