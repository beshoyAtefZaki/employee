from django import forms 

class DeductionForm(forms.Form):
	deductions = forms.DecimalField(decimal_places=2,
					label='deduction' ,
					widget=forms.NumberInput(
					attrs={"class":"form-control"}
					))


class EarningsForm(forms.Form):
	earnings = forms.DecimalField(decimal_places=2,
					label='Earning' ,
					widget=forms.NumberInput(
					attrs={"class":"form-control"}
					))

