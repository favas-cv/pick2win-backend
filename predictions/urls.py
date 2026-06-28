from django.urls import path
from .views import MyPredictionsView,CreatePredictionView,UpdatePredictionView


urlpatterns = [

    path(
        "my-predictions/",
        MyPredictionsView.as_view()
    ),

    path(
        "predict/",
        CreatePredictionView.as_view()
    ),

    path(
        "predict/<int:pk>/",
        UpdatePredictionView.as_view()
    ),
]