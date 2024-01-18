from django import forms
from django.contrib.auth.forms import  UserChangeForm, UserCreationForm
from login.models import User, Agent, Client
from mapwidgets.widgets import GooglePointFieldWidget


class AgentForm(forms.ModelForm):

    class Meta:
        model = Agent

        fields = [
            'business_name',
            'county',
            'sub_county',
            'Estate',
            'location',
            'address',
            'phone',
            'image'
        ]

    def save(self, user=None):
        agent = super(AgentForm, self).save(commit=False)
        if user:
            agent.user = user
        agent.save()
        return agent


#class AgentAdminForm(forms.ModelForm):
#    class Meta:
#        model = location
#        fields = ("coordinates", "city_hall")
#        widgets = {
#                    'coordinates': GooglePointFieldWidget,
#        'city_hall': GooglePointFieldWidget,
#        }

