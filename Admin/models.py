from django.db import models
from base.models import *

class FeaturedAd(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    vendor_name = models.ForeignKey(VendorUser, on_delete=models.CASCADE)
    priority = models.IntegerField()
    end_time = models.DateTimeField(auto_now_add=False)
    completed = models.BooleanField()
