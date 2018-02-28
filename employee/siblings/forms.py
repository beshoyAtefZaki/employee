from django import forms 
from . models import Sibilings , RELATION_CHOICES

class SibilingsForm (forms.Form):
		
	relation  = forms.CharField(
					label='Relation' ,
					widget=forms.Select(
					choices=RELATION_CHOICES,
					attrs={"class":"form-control"
					}))
	full_name  = forms.CharField(
					label='Full Name' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Full Name"}))
	age  = forms.CharField(label='Age' ,
				widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Age"}))
	nationality = forms.CharField(label='Nationality' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Nationality"}))