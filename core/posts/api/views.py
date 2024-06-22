from rest_framework import viewsets
from ..models import Post
from .serializers import PostSerializers
from rest_framework.decorators import action


class PostsViewsets(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializers


    @action(methods=['post'],detail=True)
    def like_post(self,request,pk):
        post=self.get_object()
        # add logic latter
