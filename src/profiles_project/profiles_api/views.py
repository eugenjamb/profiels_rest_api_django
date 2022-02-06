from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            'Users HTTP methods as function (get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'api_view': an_apiview})

    def post(self, request):
        """create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating the object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles updating the given object fields"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes the object"""

        return Response({'method': 'delete'})


class HelloViewSets(viewsets.ViewSet):
    """Test api view sets"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewSet': a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """gets object by id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """updates object by id"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """updates part of an object by id"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """removes object by id"""

        return Response({'http_method': 'DELETE'})


class UserProfileVewSet(viewsets.ModelViewSet):
    """creates, reads, updates profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginVewSet(viewsets.ViewSet):
    """creates and updates an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use ObtainAuthToken to validate and create a token"""

        return ObtainAuthToken().post(request)


class UserProfileFeedItem(viewsets.ModelViewSet):
    """Handles creating, reading, updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.ProfilesFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user to the logged in user"""

        serializer.save(user_profiles=self.request.user)
