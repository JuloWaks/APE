from django.shortcuts import render
from gpgsign.models import Person
from django.http import HttpResponseRedirect
from forms import PersonForm

# Create your views here.
def me(request):	
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = PersonForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = PersonForm() # An unbound form

    return render(request, 'gpgsign/person.html', {
        'form': form,
    })

def index(request):
	p = Person.objects.all()
	
	return render(request,'gpgsign/index.html',{'personas':p})