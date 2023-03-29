from django.shortcuts import render
# from django.contrib import messages
from commmunicate import message

# Create your views here.

def control_robot(request):
    
    #if request.method == 'POST':
    
    message_to_send = ''
    
    if 'forward' in request.POST:
        message_to_send = 'forward'
        
    elif 'backward' in request.POST:
        message_to_send = 'backward'
        
    elif 'right' in request.POST:
        message_to_send = 'right'
        
    elif 'left' in request.POST:
        message_to_send = 'left'   
        
    elif 'stop' in request.POST:
        message_to_send = 'stop'
    
    elif 'speed up' in request.POST:
        message_to_send = 'speed up'
        
    elif 'speed down' in request.POST:
        message_to_send = 'speed down'  
        
    if message_to_send:
        message.send_message(message=message_to_send, port='USB0')
        
    
    return render(request, template_name='page4.html')