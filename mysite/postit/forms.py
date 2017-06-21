from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import PostIt
from .choices import STATUS_CHOICES

class PostItForm(forms.ModelForm):
	class Meta:
		model = PostIt
		fields = "__all__"
		widget=forms.Select(choices=STATUS_CHOICES)
