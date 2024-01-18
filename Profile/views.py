from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy 
from random import randint
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from types import MethodType
from operator import attrgetter


class ProfileView(TemplateView):
    template_name = 'Profile/Profile.html'

    def get(self, request, category_slug=None, pk=None):
        category = None
        context = {}

        if pk:
            category = None
            user = User.objects.get(pk=pk)
        
        else:
            category = None
            user = request.user

        args = {
            'user' : user, 'category' : category
        }   
        return render(request, self.template_name, args)


def allagents(request):

    try:

        users = User.objects.exclude(id=request.user.id)
    except:
        users = User.objects.all()
    

    return render(request, 'Profile/shop.html', {'users': users})