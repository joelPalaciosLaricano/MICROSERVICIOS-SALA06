from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Campos que se muestran en la lista de usuarios
    list_display = ("email", "is_admin", "is_active") # Solo campos seguros
    ordering = ("email",)
    search_fields = ("email",)
    
    # Anulamos completamente las listas de filtros y de campos horizontales
    list_filter = ('is_active', 'is_admin',) 
    filter_horizontal = ()
    
    # Anulamos la configuración de campos para que solo use los que definiste:
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        # Usamos solo campos que sabemos que existen en AbstractBaseUser o tu modelo
        ("Permissions", {"fields": ("is_active", "is_admin")}), 
    )
    


admin.site.register(User, UserAdmin)