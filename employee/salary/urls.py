from django.conf.urls import url
from .views import (add_salary,
				SalaryDeatailView,
				add_earning ,
				add_deduction)

urlpatterns = [
 url(r'add$',add_salary, name='add') ,
 url(r'earning$',add_earning, name='earning') ,
 url(r'deduction$',add_deduction, name='deduction') ,
  url(r'detail/(?P<pk>\d+)/$',SalaryDeatailView.as_view(), name='detail') ,
]