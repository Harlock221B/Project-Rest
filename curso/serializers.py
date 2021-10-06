from rest_framework import serializers
from .models import *

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "email":{"write_only":True}
        }
    model = Avaliacao
    field = {
        'id',
        'curso',
        'nome',
        'email',
        'comentarios',
        'nota',
        'create',
        'ativo',
    }

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "email":{"write_only":True}
        }
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'create',
            'ativo',
        )