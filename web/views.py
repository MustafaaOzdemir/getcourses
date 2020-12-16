from django.shortcuts import render
from web.models import Course


# Create your views here.
def index(request):
    """View function for home page of site."""
    courses = Course.objects.all()
    print(courses[0])
   
    
   
    context = {
        'web': 1,
        'courses':courses ,

        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)