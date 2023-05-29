from django import forms
from .models import users1
class usersform(forms.ModelForm):
  class Meta:
    model = users1
    fields = "__all__"

