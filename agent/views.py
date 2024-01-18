from django.shortcuts import render
from sci import settings 
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from login.models import User 
#from .filters import UserFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from .models import Chat

def all_agents(request):
    
    return render(request, 'agent/all_agents.html')

def agent(request):
    
 
    return render(request,'agent/agent.html')

#def Git(request):
 #   return render(request, )

def agentadmin(request):
    c = Chat.objects.all()
    return render(request, 'agent/agentadmin.html', {'agentadmin': 'active', 'chat': c})


def Post(request):
    message = msg
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(id=request.user.id)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be a POST!')



def Messages(request):
    c = Chat.objects.all()
    return render(request, 'agent/message.html', {'chat': c})

