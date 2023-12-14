from django.contrib import admin
from .models import User,Works,Gallery,Service,Foryou,Blog
# Register your models here.

admin.site.register(User)
admin.site.register(Service)
admin.site.register(Foryou)
admin.site.register(Blog)
admin.site.register(Works)
admin.site.register(Gallery)
