from django.shortcuts import render
from django.http import JsonResponse
from .models import Vender_Model,PO_Model,Performance_Model
from firstApp.serializer import VenderSerializers,POSerializer,PerformanceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins

from django.db.models import Avg, Count
from django.utils import timezone
from datetime import date,timedelta
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class VenderList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset=Vender_Model.objects.all()
    serializer_class=VenderSerializers
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
    
class VenderDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset=Vender_Model.objects.all()
    serializer_class=VenderSerializers

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    
    


class PurchaseOrderList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=PO_Model.objects.all()
    serializer_class=POSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    
    
class PurchaseOrderDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset=PO_Model.objects.all()
    serializer_class=POSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
    permission_classes=[IsAuthenticated]
    

class Performance(generics.RetrieveAPIView):
    queryset = Vender_Model.objects.all()
    serializer_class = VenderSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        performance_data = {
            'date':calculate_date(instance),
            'on_time_delivery_rate': calculate_on_time_delivery_rate(instance),
            'quality_rating_avg': calculate_quality_rating_avg(instance),
            'average_response_time': calculate_average_response_time(instance),
            
            
            'fulfillment_rate': calculate_fulfillment_rate(instance)
        }
        return Response(performance_data)
    
def calculate_date(vendor):
    dt=date.today()
    return dt
    
def calculate_on_time_delivery_rate(vendor):
    completed_orders = PO_Model.objects.filter(vendor=vendor, status='completed')
    total_completed_orders = completed_orders.count()
    if total_completed_orders == 0:
        return 0
    on_time_deliveries = completed_orders.filter(delivery_date__lte=timezone.now()).count()
    on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100
    save_historical_performance(vendor, 'on_time_delivery_rate', on_time_delivery_rate)
    return on_time_delivery_rate

def calculate_quality_rating_avg(vendor):
    completed_orders = PO_Model.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    if completed_orders.count() == 0:
        return 0
    quality_rating_avg = completed_orders.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
    save_historical_performance(vendor, 'quality_rating_avg', quality_rating_avg)
    return quality_rating_avg



def calculate_fulfillment_rate(vendor):
    total_orders = PO_Model.objects.filter(vendor=vendor).count()
    if total_orders == 0:
        return 0
    fulfilled_orders = PO_Model.objects.filter(vendor=vendor, status='completed', issue_date__isnull=False)
    fulfillment_rate = (fulfilled_orders.count() / total_orders) * 100
    save_historical_performance(vendor, 'fulfillment_rate', fulfillment_rate)
    return fulfillment_rate

def save_historical_performance(vendor, metric, value):
    Performance_Model.objects.create(
        vendor=vendor,
        date=timezone.now(),
        **{metric: value}
    )

def calculate_average_response_time(vendor):
    completed_orders = PO_Model.objects.filter(vendor=vendor, status='completed', acknowledgment_date__isnull=False)
    total_completed_orders = completed_orders.count()

    # If there are no completed orders or all completed orders have null acknowledgment_date, return 0
    if total_completed_orders == 0:
        return 0
    
    total_response_time = timedelta()

    # Calculate the total response time
    for order in completed_orders:
        if order.acknowledgment_date:
            total_response_time += order.acknowledgment_date - order.issue_date

    # Calculate the average response time
    average_response_time = total_response_time.total_seconds() / total_completed_orders

    # Save the calculated average response time as historical performance
    save_historical_performance(vendor, 'average_response_time', average_response_time)
    
    return average_response_time


def index(request):
    #return HttpResponse("this is about")
    return render(request,'index.html')