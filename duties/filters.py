import django_filters

from .models import *

class dutyFilter(django_filters.FilterSet):
    class Meta:
        model = duty
        fields= ['notes']
