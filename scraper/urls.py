from django.urls import path
from .views import GPUDataView,index

urlpatterns = [
    path('', index, name='index'),
    path('gpus/', GPUDataView.as_view(), name='gpu_data'),
]