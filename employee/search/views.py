from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from mainapp.models import Employee

def search_api(request):
	if request.is_ajax():
		qs = request.GET.get('q')

		if qs :
			employee = Employee.objects.search(qs)
			employees = [
			 {
			 "full_name":e.full_name() ,
			"national_id":e.national_id ,
			"position":e.position,
			"url":e.get_absolute_url(),
			} for e in employee ]
			employee_data = {"q":qs ,
							"employees":employees}

			return JsonResponse(employee_data)
		else:
			employee = Employee.objects.all()
			employees = [
			 {
			 "full_name":e.full_name() ,
			"national_id":e.national_id ,
			"position":e.position,
			"url":e.get_absolute_url(),
			} for e in employee ]
			employee_data = {"q":qs ,
							"employees":employees}

			return JsonResponse(employee_data)
	pass
class SearchEmployeeListView(ListView):
	template_name= 'search/view.html'
	def get_queryset(self,*args,**kwargs):
		request = self.request
		qs = request.GET.get('q')
		if qs is not None and len(qs)!= 0 :
			return Employee.objects.search(qs)
		else :
			return Employee.objects.all()

	def get_context_data(self,*args,**kwargs):
		context = super( SearchEmployeeListView ,
			 self).get_context_data(*args,**kwargs)
		q = self.request.GET.get('q')
		context['q'] = q
		return context
