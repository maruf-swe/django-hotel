from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactDetail
from .forms import ContactForm
from django.core.mail import send_mail as sm, BadHeaderError


def send_mail(request):
	contact_details = ContactDetail.objects.last()
	template = 'contact/contact.html'

	if request.method =='POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			subject = contact_form.cleaned_data['subject']
			from_email = contact_form.cleaned_data['from_email']
			message = contact_form.cleaned_data['message']

			try:
				sm(subject, message, from_email, ['test@gmail.com'])

			except BadHeaderError:
				return HttpResponse("Invalid Something")

			return redirect('contact:success')

	else:
		contact_form = ContactForm()


	context = {
		'contact_details' : contact_details,
		'contact_form' : contact_form
	}

	return render(request, template, context)


def success(request):
	return HttpResponse("Message sent Successfully")
