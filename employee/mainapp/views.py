from django.shortcuts import render ,redirect
from django.views.generic import ListView ,DetailView
from django.http import Http404
from django.views.generic.edit import CreateView
from .models import Employee
from .forms import EmployeeForm
from siblings.models import Sibilings
from siblings.forms import SibilingsForm
from django.contrib import messages
from salary.models import Salary
#adding apis to this model 
from rest_framework import generics
from .serilizers import  EmployeeSerialzier

def home(request):
	form = EmployeeForm()
	qs = Employee.objects.all()
	content={
	'form':form,
	'objects': qs
	} 
	return render(request,'mainapp/home.html',content)

def create(request):
	form = EmployeeForm(request.POST or None)
	if form.is_valid():
		first_name		= form.cleaned_data.get('first_name')
		last_name 		= form.cleaned_data.get('last_name')
		middle_name		= form.cleaned_data.get('middle_name')
		image			= request.FILES['image']
		national_id 	= form.cleaned_data.get('national_id')
		position 		= form.cleaned_data.get('position')
		jop 			= form.cleaned_data.get('jop')
		age				= form.cleaned_data.get('age')
		date_of_birth 	= form.cleaned_data.get('date_of_birth')
		place_of_birth  = form.cleaned_data.get('place_of_birth')
		country			= form.cleaned_data.get('country')
		nationality 	= form.cleaned_data.get('nationality')
		maritial_status = form.cleaned_data.get('maritial_status')
		gendar 			= form.cleaned_data.get('gendar')
		Employee.objects.create(first_name=first_name ,
						last_name=last_name,
						middle_name=middle_name,
						image=image,
						national_id=national_id,
						position=position.lower(),
						jop=jop,
						age=age,
						date_of_birth=date_of_birth,
						place_of_birth=place_of_birth,
						country = country ,
						nationality=nationality,
						maritial_status=maritial_status,
						gendar=gendar,
								)
		employee = Employee.objects.get(national_id=national_id)
		return render (request,'salary/add_main_salary.html',{'employee':employee})
		
	return render(request,'mainapp/createemploye.html' , {'form':form})


def update_view(request ,slug=None):
	qs = Employee.objects.filter(slug=slug)
	employe = qs.first()
	if request.method =='POST':
		if (request.POST.get('position')):
			employe.position = request.POST.get('position')
		if (request.POST.get('jop')):
			employe.jop = request.POST.get('jop')	
		if (request.FILES.get('image')):
			employe.image = request.FILES.get('image')	
		if (request.POST.get('maritial_status')):
			employe.maritial_status = request.POST.get('maritial_status')
		else:
			return redirect ("home")
		employe.save()
		return redirect(employe.get_absolute_url())
	content = {
	'employee':employe,
	'main_view' : True
	}
	return render(request,'mainapp/update.html' ,content)

def delete_view(request):
	if request.method =='POST':
		employee_id =request.POST.get('employee_id')
		qs = Employee.objects.filter(id=employee_id)
		employe = qs.first()
		if employe.jop :
			messages.add_message(request,messages.INFO,'you cant delete this employee')
			return redirect(employe.get_absolute_url())
		else :
			Employee.objects.filter(id=employee_id).delete()
	return redirect("home")



class EmployeeDetailView(DetailView):
	template_name= 'mainapp/detailview.html'

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		qs = Employee.objects.filter(slug=slug)
		if qs.count() != 1:
			raise Http404("Employee doesn't exist !")	
		return qs.first()

	def get_context_data(self,*args,**kwargs):
		context = super( EmployeeDetailView ,
			 self).get_context_data(*args,**kwargs)
		e = context.get('object')
		qs = Sibilings.objects.filter(employee=e)
		form = SibilingsForm()
		s_info = Salary.objects.filter(employee=e)
		salary_info =s_info.first()		
		context['sibilings'] 	= qs
		context['form']			= form
		context['salary_info']	= salary_info

		
		return context



#create the api view 
class EmployeeApi(generics.RetrieveUpdateDestroyAPIView):
	lookup_field	= 'pk'
	queryset		=  Employee.objects.all()
	serializer_class = EmployeeSerialzier