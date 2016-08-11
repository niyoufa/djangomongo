#coding=utf-8

import pdb,json

from dhuicredit.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    create_date = serializers.SerializerMethodField()
    login_date = serializers.SerializerMethodField()
    write_date = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    user_auth_type = serializers.SerializerMethodField()

    def get_id(self,instance):
        return str(instance.id)

    def get_create_date(self,instance):
        if instance.create_date == "":
            return ""
        else:
            return str(instance.create_date)

    def get_login_date(self, instance):
        if instance.login_date == "":
            return ""
        else:
            return str(instance.login_date)

    def get_write_date(self, instance):
        if instance.write_date == "":
            return ""
        else:
            return str(instance.write_date)

    def get_type(self,instance):
        return instance.type

    def get_user_auth_type(self,instance):
        return instance.user_auth_type

    class Meta:
        model = User
        fields = ("id","mobile","email","type","province","city","create_date","invitation_mobile",
                  "login_date","address",
                  "sex","privilege","active","write_date",
                  "headimageurl","password","nickname",
                  "user_auth_type","type")