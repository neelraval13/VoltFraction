from django.contrib import admin

# Register your models here.

from .models import Member, Announcement, Game, Tier, Profile

admin.site.register(Game)
admin.site.register(Tier)
admin.site.register(Member)
admin.site.register(Announcement)
admin.site.register(Profile)