from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Person, Category
from .serializers import PoetSerializers



class CRUDPoet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    serializer_class = PoetSerializers

    def get_queryset(self):
        return Person.objects.all()

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class ListCreatePoet(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
#
# class UpdataPoet(generics.UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
#
# class DeleteRetrivePoet(generics.RetrieveDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers




