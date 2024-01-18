from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


from login.decorators import client_required, agent_required
from login.models import Agent, User
from django.views.generic import TemplateView , CreateView
from login.forms import AgentSignUpForm


class AgentSignUpView(CreateView):
    template_name = 'registration/signup_form.html'
    model = Agent
    form_class = AgentSignUpForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('agent:product_list')



