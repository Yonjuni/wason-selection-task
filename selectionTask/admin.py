from django.contrib import admin

from models import AbstractTask, ConcreteTask, Subject, Result

admin.site.register(AbstractTask)
admin.site.register(ConcreteTask)
admin.site.register(Subject)
admin.site.register(Result)