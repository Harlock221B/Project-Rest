from django.urls import path, include
from .views import CursoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('cursos/',CursoAPIView.as_view(),name='cursos'),
    path('avaliacao/',AvaliacaoAPIView.as_view(),name='avaliacao'),
]
