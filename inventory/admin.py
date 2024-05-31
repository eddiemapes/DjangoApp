from typing import Any
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpRequest
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)
admin.site.register(Profile)

# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend user model 
class UserAdmin(BaseUserAdmin):
    # model = User
    # fields = ['username', 'first_name', 'last_name', 'email']
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Unregister old way
admin.site.unregister(User)

# Register new way 
admin.site.register(User, UserAdmin)


