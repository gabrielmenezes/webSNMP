from django.db import models

# Create your models here.


class Device(models.Model):
    device_name = models.CharField(max_length=255)
    device_ip = models.CharField(max_length=255)

    def __str__(self):
        return self.device_name + ' - ' + self.device_ip


class SNMPInfo(models.Model):
    oid_name = models.CharField(max_length=255)
    oid = models.CharField(max_length=255)
    returnValue = models.CharField(max_length=255)

    def __str__(self):
        return self.oid_name
