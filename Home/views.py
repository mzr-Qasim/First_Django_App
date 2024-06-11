from django.http import HttpResponse
from django.template import loader

# Create your views here.
def  homePage(request):
    Page=loader.get_template('Website/index.html')
    return HttpResponse(Page.render())