from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import PerfilUsuario, Azucar, GlutenFree, Vegano  # Importa tu modelo de perfil de usuario



# Registrar el perfil de usuario en el admin
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario  # El modelo de perfil que contiene información extra
    can_delete = False
    verbose_name_plural = 'Perfiles de Usuarios'

# Extendemos la clase del admin de usuarios de Django para incluir el perfil de usuario
class UsuarioAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline,)  # Agregamos el perfil como una sección dentro del usuario

# Volvemos a registrar el modelo de usuario con la clase UsuarioAdmin
admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)


# Registramos el modelo Azucar en el admin
class AzucarAdmin(admin.ModelAdmin):
    list_display = ('nombre_comercio', 'nombre_producto', 'fecha_subida', 'precio')

admin.site.register(Azucar, AzucarAdmin)

# Registramos el modelo Vegano en el admin
class VeganoAdmin(admin.ModelAdmin):
    list_display = ('nombre_comercio', 'nombre_producto', 'fecha_subida', 'precio')

admin.site.register(Vegano, VeganoAdmin)

# Registramos el modelo GlutenFree en el admin
class GlutenFreeAdmin(admin.ModelAdmin):
    list_display = ('nombre_comercio', 'nombre_producto', 'fecha_subida', 'precio')

admin.site.register(GlutenFree, GlutenFreeAdmin)
