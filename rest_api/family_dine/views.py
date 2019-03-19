from django.http import Http404, JsonResponse, QueryDict
from rest_framework import generics, permissions, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Dine, DineLocation
from .serializer import DineSerializer, DineLocationSerializer
from .permissions import IsOwnerOrReadOnly


class DineList(generics.ListCreateAPIView):
    queryset = Dine.objects.all().order_by('date')
    serializer_class = DineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDineList(DineList):
    def get_queryset(self):
        owner = User.objects.get(username=self.kwargs['username'])
        return Dine.objects.filter(owner=owner).order_by('date')


class DineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dine.objects.all()
    serializer_class = DineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class DineLocationList(generics.ListCreateAPIView):
    queryset = DineLocation.objects.all()
    serializer_class = DineLocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class JoinDine(APIView):

    def get_object(self, pk):
        try:
            return Dine.objects.get(pk=pk)
        except Dine.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        dine = self.get_object(pk)
        # print(dine.participant.all())
        data = json.loads(request.body)
        flag = data['isJoined']

        if flag:
            dine.participant.remove(request.user)
        else:
            dine.participant.add(request.user)

        serializer = DineSerializer(dine)
        # serializer = JoinDineSerializer(dine, data={"username": "noke"})
        # if serializer.is_valid():
        #     serializer.save()
        #     print("valid")
        #     return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



