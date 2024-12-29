from django.contrib import admin
from .models import Matriz, Element

class MatrizAdmin(admin.ModelAdmin):
    pass

class ElementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Matriz, MatrizAdmin)
admin.site.register(Element, ElementAdmin)
