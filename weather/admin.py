from django.contrib import admin
from .models import Schedule, Dailyweatherforecast, Hourlyweatherforecast

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Dailyweatherforecast)
admin.site.register(Hourlyweatherforecast)
