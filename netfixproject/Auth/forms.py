from django import forms
from .models import Register
class register(forms.ModelForm):
    class meta :
        model = Register
        fields ='__all__'