# rest
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# apps
from .models import Video
from .serializers import VideoSerializer


class ListVideo(APIView):
    def get(self, request):
        """
        endpoint: Me permite obtener todos los videos
        :return videos en formato json
        """
        videos = Video.objects.all()
        video_json = VideoSerializer(videos,
                                     many=True)  # MarshalL -> serializamos el objeto. Esta clase nos regresará un objeto serializado, el campo many es pq son varios objetos q se serializan
        return Response(video_json.data)

    def post(self, request):
        """
        endpoint: Me permite crear un video
        :return video en formato json
        """
        video_json = VideoSerializer(data=request.data, many=True)  # UnMarshall
        if video_json.is_valid():  # si lo q nos envió el usr es correcto
            video_json.save()  # guardamos en la bd
            return Response(video_json.data, status=201)  # se creó un nuevo registro le damos el status 201
        return Response(video_json.errors, status=400)


class DetailVideo(APIView):
    def get_object(self, pk):
        """
        Filtra los videos existentes
        """
        try:
            return Video.objects.get(pk=pk)  # filtrame por id
        except Video.DoesNotExist:  # si no existe el video
            raise Http404

    def get(self, request, pk):
        """
        endpoint: Me permite obtener el detalle de un video
        :return un video en formato json. Si no existe devuelve un 404
        """
        try:
            video = self.get_object(pk)
            video_json = VideoSerializer(video)  # serializamos un único objeto
            return Response(video_json.data)
        except Video.DoesNotExist:  # si no existe el video
            raise Http404

    def put(self, request, pk):
        """
        endpoint: Me permite actualizar el detalle de un video
        :return un video en formato json. Si no existe devuelve un 404
         """
        try:
            video = self.get_object(pk)  # filtrame por id
            video_json = VideoSerializer(video,
                                         data=request.data)  # Acá VideoSerializer toma todos los datos que nuestro usr nos envie y los almacena en el objeto video
            if video_json.is_valid():
                video_json.save()
                return Response(video_json.data)
            # else
            return Response(video_json.errors, status=400)

        except Video.DoesNotExist:  # si no existe el video
            raise Http404

    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=204) #status 204 -> no encontró ningun contenido