from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=2)
    createTime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        if self.name:
            return "%d, %s, %d, %s" % (self.id, self.name, self.age, str(self.createTime))
        else:
            return ""


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    createTime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        if self.name:
            return "%d, %s, %s" % (self.id, self.name, str(self.createTime))
        else:
            return ""