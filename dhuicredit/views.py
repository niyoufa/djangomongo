#coding=utf-8

import pdb, json, datetime

from dhuicredit.models import User
from dhuicredit.serializers import UserSerializer
from django.shortcuts import render,render_to_response

from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.using("dhuicredit").all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.using("dhuicredit").all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        try:
            if not serializer.instance.write_date :
                serializer.instance.write_date = datetime.datetime.now()
                serializer.instance.save()
        except:
            pass
        serializer.save()
