from django.views.generic import TemplateView

# create a simple view to handle homepage
class HomePage(TemplateView):
    template_name = 'index.html'