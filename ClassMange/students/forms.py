from django.forms import ModelForm
from .models import Stu


class AddForms(ModelForm):
    class Meta:
        model = Stu
        fields = '__all__'
