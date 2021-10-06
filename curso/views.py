from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import *
from rest_framework import status

class CursoAPIView(APIView):

    def get(self, request):
        curso = Curso.objects.all()
        serializers = CursoSerializer(curso, many=True)

        return Response(serializers.data)

class AvaliacaoAPIView(APIView):
    def get(self, request):
        av = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(av, many=True)
        # gerando JSON
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.valid(raise_exception=True)
        serializer.save()
        # return Response({"msg": "Inserido com sucesso"})
        return Response({"msg":"Insirido com sucesso"})
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
# Create your views here.
