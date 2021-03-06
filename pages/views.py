from django.views.generic import TemplateView
from django.views.generic import ListView

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from trails import models

class HomePageView(ListView):
    model = models.Trail
    template_name = 'home.html'
    ordering = ['-date']

class AboutPageView(TemplateView):
	template_name = 'about.html'

class ContactPageView(TemplateView):
	template_name = 'contact.html'

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['silviu.wagner@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# class StoryPageView(TemplateView):
# 	template_name = 'story.html'

# class TeamPageView(TemplateView):
# 	template_name = 'team.html'