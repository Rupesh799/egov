from django.contrib import admin
from account.models import User,Problems,alert
# Register your models here.
admin.site.register(User)
admin.site.register(Problems)
admin.site.register(alert)
