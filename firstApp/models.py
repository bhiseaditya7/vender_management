from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.
class Vender_Model(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField(max_length=100)
    address=models.TextField(max_length=100)
    vender_code=models.IntegerField(primary_key=True,unique=True)
    on_time_delivery_rate=models.FloatField(max_length=60,null=True)
    quality_rating_avg=models.FloatField(max_length=10,null=True)
    average_response_time=models.FloatField(max_length=60,null=True)
    fulfillment_rate=models.FloatField(max_length=100,null=True)

class PO_Model(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    
    po_number=models.CharField(primary_key=True,unique=True)
    vendor=models.ForeignKey(Vender_Model,on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES, default='pending')
    quality_rating=models.FloatField(null=True)
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField(null=True)




class Performance_Model(models.Model):
    vendor=models.ForeignKey(Vender_Model,on_delete=models.CASCADE)
    
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField(max_length=60,null=True)
    quality_rating_avg=models.FloatField(null=True)
    average_response_time=models.FloatField(null=True)
    fulfillment_rate=models.FloatField(null=True)

@receiver(post_save,sender= settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)