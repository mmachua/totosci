from django.contrib import admin
from login.models import Agent, Client, User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'username', 'first_name', 'last_name' ,'email','is_client', 'is_agent')

    def user_info(self, obj):
        return obj.description

def get_queryset(self, request):
    queryset = super(UserAdmin, self).get_queryset(request)
    queryset = queryset.order_by('username', 'first_name')
    return queryset
    

admin.site.register(User, UserAdmin)


class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', 'county' ,'sub_county','location','address', 'phone')

    def user_info(self, obj):
        return obj.description

admin.site.register(Agent, AgentAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('user','gender' , 'county', 'phone')

    def user_info(self, obj):
        return obj.description

admin.site.register(Client, ClientAdmin)



