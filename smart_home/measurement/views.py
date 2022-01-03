from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorListSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView



class SensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

    def sensor_create(self, serializer):
        serializer.save()

class SensorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



class MeasurementList(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def measurement_create(self, serializer):
        serializer.save()


