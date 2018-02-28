from rest_framework import serializers
from .models import Employee
class EmployeeSerialzier(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields= [
			'pk',
			'first_name',
			'last_name',
			'middle_name',
			'slug',
			'image',
			'national_id',
			'position',
			'age',
			'date_of_birth',
			'timestamp',
			'place_of_birth',
			'country',
			'nationality',
			'maritial_status',
			'gendar',


			]
		read_only_fields =['first_name',
						'last_name','middle_name',
						'national_id','age','slug']