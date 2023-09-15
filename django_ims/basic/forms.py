from django.forms import ModelForm
from .models import *


class Itemform(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        