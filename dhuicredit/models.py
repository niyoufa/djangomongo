#coding-utf-8

import pdb
from django.db import models

from djangotoolbox.fields import ListField,EmbeddedModelField
from django_mongodb_engine.storage import GridFSStorage


gridfs_storage = GridFSStorage()

class User(models.Model):
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    create_date = models.DateTimeField(auto_created=True)
    login_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now_add=True)

    type = ListField()
    user_auth_type = ListField(blank=True)

    sex = models.IntegerField(blank=True,default=0)
    privilege = models.IntegerField(blank=True,default=0)
    active = models.IntegerField(blank=True,default=0)

    province = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    invitation_mobile = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=255,blank=True)
    headimageurl = models.CharField(max_length=255,blank=True)
    nickname = models.CharField(max_length=255,blank=True)

    class Meta:
        db_table = "user"

        unique_together = (("phone"),("email"))