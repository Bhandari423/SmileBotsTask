from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED,
)
from . import models
from .permissions import UpdateOwnProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class PostView(APIView):
    def post(self, request):
        post_image = request.FILES.get('image') 
        post_title = request.POST.get('title')
        post_description = request.POST.get('description')

        obj = models.PostDetail.objects.create(
            post_image=post_image,
            post_title=post_title,
            post_description=post_description,
        )
        return Response({"message": "Post created"}, status=HTTP_201_CREATED)

    def get(self,request):
        obj = models.PostDetail.objects.values()
        if obj:
            return Response({"obj": obj}, status=HTTP_200_OK)
        else:
            return Response({"error": "Not found"}, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        obj = models.PostDetail.objects.filter(id=pk)
        if obj:
            obj.delete()
            return Response({"message": "Post Deleted"}, status=HTTP_200_OK)
        else:
            return Response({"error": "Invalid Post ID"}, status=HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    def post(self, request):
        comment = request.POST.get('comment')
        obj = models.CommentDetail.objects.values()
        return Response({"message": "Comment created"}, status=HTTP_201_CREATED)