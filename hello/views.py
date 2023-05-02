from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "home.html"

class Aboutpage(TemplateView):
    template_name = "about.html"
    
class Servicespage(TemplateView):
    template_name = "service.html"
