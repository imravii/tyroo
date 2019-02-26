from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.core.urlresolvers import reverse_lazy
from django.forms import  Textarea
# Create your views here.
from home.models import Rule
from django.shortcuts import redirect

from django.shortcuts import render

# Create your views here.

from multiselectfield import MultiSelectFormField

from django.shortcuts import render, get_object_or_404
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'product_list'
    template_name = 'home/index.html'

    def get_queryset(self):
        return Rule.objects.all()

class ProductUpdate(UpdateView):
    model = Rule
    # the fields mentioned below become the entyr rows in the update form
    fields = ['Rule_name','Campaigns', 'Schedule','Conditions','Action','Status']

   # template_name_suffix = '_update_form'
class ProductDelete(DeleteView):
    model = Rule
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('home:index')

class ProductEntry(CreateView):
   model = Rule

   fields = ['Rule_name', 'Campaigns', 'Schedule','Conditions','Action','Status']
   widgets = {
       'Campaigns': MultiSelectFormField(choices=Rule.camps, max_length=11),

   }
from django.core.mail import send_mail
def fun():
    send_mail(
        'sub-Ravi-Testing of email',
        'Hello anurag... done my task of emailing in python..'
        'best regards,'
        'ravi rathore',
        'ravir.ic@nsit.net.in',
        ['ravir.ic@nsit.net.in'],
        fail_silently=False,
    )
def mainn():
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('''SELECT pk_camps FROM Camps_master''')
    c=0
    for i in cursor:
        c+=i[0]
    if(c>10):
        fun()

