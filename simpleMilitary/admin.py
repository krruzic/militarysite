from django.contrib import admin
from simpleMilitary.models import *
# Register your models here.
class PersonnelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': ['psin', 'supersin']}),
        ('Service Information',  {'fields': ['rank', 'status', 'uid']}),
    ]
    search_fields = ['psin__fname', 'psin__lname']
    list_display = ('get_fname', 'get_lname', 'get_sin')
    list_filter = ['status']
    actions = ['Personnel updated!']

    def personnel_updated(self, request, queryset):
        self.message_user(request, "Personnel successfully updated!")

    class Media:
        js = ("/static/js/hide_myfield_info.js",)

    # print submit_buttons_top

admin.site.register(Person)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Unit)