#rest
from rest_framework.views import APIView
from rest_framework.response import Response
#apps
from .models import Video
from .serializers import VideoSerializer

#endpoint
class ListVideo(APIView):
    def get(self,request):
        videos = Video.objects.all()
        video_json = VideoSerializer(videos, many=True) #MarshalL -> serializamos el objeto. Esta clase nos regresará un objeto serializado, el campo many es pq son varios objetos q se serializan
        return Response(video_json.data)

    def post(self,request):
        video_json =  VideoSerializer(data=request.data, many=True) #UnMarshall
        if video_json.is_valid():#si lo q nos envió el usr es correcto
            video_json.save() #guardamos en la bd
            return Response(video_json.data,status=201) #se creó un nuevo registro le damos el status 201
        return Response(video_json.errors,status=400)