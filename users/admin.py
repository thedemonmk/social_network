from django.contrib import admin
from .models import SocialUser, FriendRequest

class SocialUserAdmin(admin.ModelAdmin):
    search_fields = ('email',)

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'status', 'timestamp')

admin.site.register(SocialUser, SocialUserAdmin)
admin.site.register(FriendRequest)