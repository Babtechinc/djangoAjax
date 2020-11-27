from django.db import models

# Create your models here.
class Notification(models.Model):
    name = models.CharField(max_length=100)
    miniMsg = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)

    def __str__(self):
        return self.msg