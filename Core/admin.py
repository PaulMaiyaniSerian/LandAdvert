from django.contrib import admin
from .models import Contact, Land, OtherProperty,Ranch
# Register your models here.

admin.site.register(Contact)
admin.site.register(Land)
admin.site.register(OtherProperty)
admin.site.register(Ranch)