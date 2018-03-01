from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Employee

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
