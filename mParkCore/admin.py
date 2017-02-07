from django.contrib import admin
from .models import Post, Comment, Professional, Team, Patient, Session, SessionFile


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Professional)
admin.site.register(Team)
admin.site.register(Patient)
admin.site.register(Session)
admin.site.register(SessionFile)