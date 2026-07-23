from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'gender', 'birth_date', 'telnum', 'zipcode', 'base_addr', 'dtl_addr']