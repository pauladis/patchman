from django.forms import ModelForm
from .models import CompleteUser

class CompleteUserForm(ModelForm):

    class Meta:
        model = CompleteUser
        fields = '__all__'