from django.contrib import admin
from .views import Tasks, Register, Login


# Register your models here.

admin.site.register(Tasks)
admin.site.register(Register)
admin.site.register(Login)


