from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from django.shortcuts import redirect
from django.core.mail import send_mail


# Create your views here.
def home(request):
	form=SignUpForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		full_name=form.cleaned_data.get("full_name")
		# print "fullname +++++++++++++++"
		# print full_name
		if not full_name:
			full_name="full_name"
		instance.full_name=full_name	
		instance.save()
		


	context={
	"form":form
	}
	return render(request,"home.html",context)


def contact(request):
	title="Contact Us"
	form=ContactForm(request.POST or None)
	if form.is_valid():
		form_email=form.cleaned_data.get('email')
		form_message=form.cleaned_data.get('message')
		form_full_name=form.cleaned_data.get('full_name')
		subject='Site contact form'
		contact_message="%s:%s via %s"%(form_full_name,form_message,form_email)
		from_email=settings.EMAIL_HOST_USER
		to_email=[form_email,'youotheremail@gmail.com']
		send_mail(
		    'subject',
		    'contact_message',
		    'from_email',
		    'to_email',
		    fail_silently=False,
		)
	context={
	"title":title,
	"form":form,

	}
	return render(request,"form.html",context)
