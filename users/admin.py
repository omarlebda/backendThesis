from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name',
                    'last_name', 'phone_number', 'email', 'is_staff']
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            # group heading of your choice; set to None for a blank space instead of a header
            'Custom Field Heading',
            {
                'fields': (
                    'phone_number',
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
