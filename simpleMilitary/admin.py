from django.contrib import admin
from simpleMilitary.models import *
# Register your models here.
class PersonnelAdmin(admin.ModelAdmin):
    # Different form for change and add
    def get_formsets(self, request, obj=None):
        self.readonly_fields = None
        self.change_fieldsets = [
            ('Personal Information', {'fields': ['get_name', 'supersin']}),
            ('Service Information',  {'fields': ['rank', 'status', 'uid']}),
        ]
        self.add_fieldsets = [
            ('Personal Information', {'fields': ['psin', 'supersin']}),
            ('Service Information',  {'fields': ['rank', 'status', 'uid']}),
        ]
        if obj is None:
            self.fieldsets = self.add_fieldsets
        else:
            self.readonly_fields = ['get_name']
            self.fieldsets = self.change_fieldsets
        return super(PersonnelAdmin, self).get_formsets(request, obj)
    search_fields = ['psin__fname', 'psin__lname']
    list_display = ('get_fname', 'get_lname', 'get_sin')
    list_filter = ['status','rank']

    # class Media:
    #     js = ("/static/js/hide_mypersonnel_info.js",)





class PersonnelInline(admin.TabularInline):
    model = Personnel
    verbose_name_plural = 'Members'
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False

    class Media:
        js = ("/static/js/disable_inline_info.js",)

class PersonAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
    verbose_name_plural = 'Name'
    verbose_name = 'Name'

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
    extra = 0
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False

    class Media:
        js = ("/static/js/disable_inline_info.js",)


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
