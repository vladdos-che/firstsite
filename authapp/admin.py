from django.contrib import admin

from authapp.models import BbUser, Profile

admin.site.register(Profile)  # lesson_42_hw


class BbUserAdmin(admin.ModelAdmin):  # lesson_45_hw
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name')
    sortable_by = ('username', 'age')
    list_editable = ('age', 'is_staff', 'is_active')
    list_display_links = ('username', 'email')


admin.site.register(BbUser, BbUserAdmin)
