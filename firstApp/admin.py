from django.contrib import admin

# Register your models here.
from .models import Vender_Model,PO_Model,Performance_Model
admin.site.register(Vender_Model)
admin.site.register(PO_Model)
admin.site.register(Performance_Model)
