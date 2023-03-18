from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def control_robot(request):
    
    y = 0
    
    #if request.method == 'POST':
    
    if 'forward' in request.POST:
        x = 0
        
    elif 'backward' in request.POST:
        x = 0
        
    elif 'right' in request.POST:
        x = 0
        
    elif 'left' in request.POST:
        x = 0    
    
    return render(request, template_name='page2.html')