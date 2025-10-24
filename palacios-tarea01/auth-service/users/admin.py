from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Campos que se muestran en la lista de usuarios
    list_display = ("email", "is_admin", "is_active") 
    ordering = ("email",)
    search_fields = ("email",)
    

    list_filter = ('is_active', 'is_admin',) 
    filter_horizontal = ()
    

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_admin")}), 
    )
    


admin.site.register(User, UserAdmin)