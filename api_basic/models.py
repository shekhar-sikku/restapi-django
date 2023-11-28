from django.db import models


class Articles(models.Model):
    objects = None
    DoesNotExist = None
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    tag = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
