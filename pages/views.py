from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'home.html'

class StoryPageView(TemplateView):
	template_name = 'story.html'

class TeamPageView(TemplateView):
	template_name = 'team.html'

class ContactPageView(TemplateView):
	template_name = 'contact.html'