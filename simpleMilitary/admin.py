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
    list_filter = ['status','rank']
    actions = ['Personnel updated!']

    def personnel_updated(self, request, queryset):
        self.message_user(request, "Personnel successfully updated!")
    class Media:
        js = ("/static/js/hide_mypersonnel_info.js",)

    # print submit_buttons_top

class PersonAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}




class PersonnelInline(admin.TabularInline):
    model = Personnel
    verbose_name_plural = "Members"
    readonly_fields = ('psin', 'rank', 'status', 'supersin',)
    extra = 0
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False

class UnitAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Unit Information', {'fields': ['uid', 'uname', 'type', 'bid', 'cid', 'commander_sin']})]
    search_fields = ['uname']
    list_display = ('uname', 'type', 'get_bname', 'get_cname', 'uid')
    list_filter = ['type']
    inlines = [PersonnelInline]
    class Media:
        js = ("/static/js/hide_myunit_info.js",)



class UnitInline(admin.TabularInline):
    model = Unit
    readonly_fields = ('uname', 'type', 'get_cname', 'cid', 'commander_sin', 'uid')
    extra = 0
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False

class BaseAdmin(admin.ModelAdmin):
    search_fields = ['bname','location']
    list_display = ('bname', 'type', 'location', 'bid')
    list_filter = ['type']
    inlines = [UnitInline]
    class Media:
        js = ("/static/js/hide_mybase_info.js",)





admin.site.register(Person, PersonAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Conflict)
admin.site.register(Equipment)
admin.site.register(Operations)
admin.site.register(Award)
admin.site.register(Veteran)
