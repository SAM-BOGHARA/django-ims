from django.forms import ModelForm
from .models import *


class Itemform(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ["name", "itemname", "description", "quantity","category"]


class RequestFormUpdate(ModelForm):
    class Meta:
        model = Request
        fields = "__all__"
