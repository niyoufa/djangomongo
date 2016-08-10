#coding-utf-8

import pdb
from django.db import models

from djangotoolbox.fields import ListField,EmbeddedModelField
from django_mongodb_engine.storage import GridFSStorage


gridfs_storage = GridFSStorage()

class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    tags = ListField()
    comments = ListField()
    author = EmbeddedModelField('Author')

class Author(models.Model):
    name = models.CharField()

class FileUpload(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=gridfs_storage, upload_to='/')

