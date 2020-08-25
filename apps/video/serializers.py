from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Video

class UserSerializer(serializers.ModelSerializer):
    """
    Me permite obtener los usuarios que están relacionados con un video
    """
    class Meta:
        model = User
        fields = ('id','username','email')

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) #con esto obtengo el objeto de usuario para ver en el json, si no me devuelve el pk del usuario
    class Meta:
        model = Video
        fields = ('id','title','description','user')