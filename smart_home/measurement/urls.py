from django.urls import path

from .views import SensorsList, SensorDetail, MeasurementList
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>', SensorDetail.as_view()),
    path('measurements/', MeasurementList.as_view()),

]
