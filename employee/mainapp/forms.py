from django import forms 
import datetime
from .models import (Employee ,
					POSITION_CHOICES ,
					GENDAR_COICES ,
					MARIRTIAL_STATUS_CHOICES)



Birth_year_choice =tuple(
	str(i + 1978) for i in range(30)
						)


class EmployeeForm (forms.Form):
	
		
	first_name  = forms.CharField(
					label='First Name' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"First Name"}))
	last_name  = forms.CharField(
					label='Last Name' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Last Name"}))
	middle_name = forms.CharField(
					label='Middle Name' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Middle Name"}))
	image       =forms.FileField(label='Imagee' ,
					required=False,
					widget=forms.ClearableFileInput(
					attrs={'multiple':True,
					"class":"form-control"
					,"placeholder":"Imagee"}))
	national_id =forms.IntegerField(
					label='National Id' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"National Id"}))
	position  = forms.CharField(label='Position' ,
					widget=forms.Select(
					choices=POSITION_CHOICES,
					attrs={"class":"form-control",
					}))
	jop  = forms.CharField(label='Jop' ,
					required=False,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Jop"}))
	age  = forms.CharField(label='Age' ,
				widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Age"}))
	date_of_birth = forms.DateField(
					widget=forms.SelectDateWidget(
					years=Birth_year_choice,
					attrs={"class":"form-control" 
							,"value":"1992-8-12"}))
	place_of_birth = forms.CharField(
					label='place of birth' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"place of birth"}))

	country= forms.CharField(label='Country' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Country"}))

	nationality = forms.CharField(label='Nationality' ,
					widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Nationality"}))
	maritial_status= forms.CharField(
					label='Maritial Status' ,
					widget=forms.Select(
					choices=MARIRTIAL_STATUS_CHOICES,
					attrs={"class":"form-control"
					}))
	gendar = forms.CharField(label='Gender' ,
					widget=forms.Select(
					choices=GENDAR_COICES,
					attrs={"class":"form-control"
					}))


	def clean_national_id(self):
		national_id= self.cleaned_data.get(
					'national_id')
		qs =Employee.objects.filter(national_id=national_id)


		if qs.count()==1 :
			raise forms.ValidationError('national id invalid')
		return national_id 