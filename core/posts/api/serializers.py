from rest_framework import serializers
from ..models import Post   


class PostSerializers(serializers.ModelSerializers):
    class Meta:
        model=Post
        fields=('id','title','body','like','author')