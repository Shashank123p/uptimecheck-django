from django.shortcuts import render
from rest_framework import viewsets
from uptime.models import websites
from uptime.serializers import WebsiteSerializer,UserSerializer
from rest_framework import generics, parsers, renderers, status
from django.contrib.auth import get_user_model
# Create your views here.

class WebsitesDataView(viewsets.ModelViewSet):
    model = websites
    serializer_class = WebsiteSerializer

    def get_queryset(self):
        queryset = websites.objects.all()
        return queryset


class UserList(generics.ListAPIView):
    """
    get:
        Return all users, ordered by username
    """
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ( )

    serializer_class = UserSerializer

    def get_queryset(self):
        User = get_user_model()
        user_search = self.request.query_params.get('q', None)

        if user_search:
            return User.objects.filter(
                Q(username__contains=user_search)
            )
        return User.objects.all()
