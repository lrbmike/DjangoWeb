from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
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


class Grade(models.Model):
    name = models.CharField(max_length=50)
    teacherId = models.IntegerField(null=True)
    userId = models.IntegerField(null=True)
    createTime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        if self.name:
            return "%d, %s, %d, %d, %s" % (self.id, self.name, self.teacherId, self.userId, str(self.createTime))
        else:
            return ""