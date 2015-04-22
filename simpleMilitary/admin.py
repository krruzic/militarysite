from django.contrib import admin
from simpleMilitary.models import *
# Register your models here.

class SuperviseeInline(admin.TabularInline):
    list_select_related = True
    model = Personnel
    verbose_name_plural = 'Supervisees'
    extra = 0
    def get_queryset(self, request):
        return super(SuperviseeInline, self).get_queryset(request).select_related()
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    class Media:
        js = ("/static/js/disable_inline_info.js",)

class AuthorizedInline(admin.TabularInline):
    model = AuthorizedToUse
    verbose_name_plural = 'Equipment Permissions'
    extra = 0
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    class Media:
        js = ("/static/js/disable_inline_info.js",)



class PersonnelAdmin(admin.ModelAdmin):
    # Different form for change and add
    def get_queryset(self, request):
        return super(PersonnelAdmin, self).get_queryset(request).select_related('psin', 'uid', 'supersin')
    def get_formsets(self, request, obj=None):
        self.readonly_fields = None
        self.change_fieldsets = [
            ('Personal Information', {'fields': ['get_name', 'supersin']}),
            ('Service Information',  {'fields': ['rank', 'status', 'uid', 'get_awards']}),
        ]
        self.add_fieldsets = [
            ('Personal Information', {'fields': ['psin', 'supersin']}),
            ('Service Information',  {'fields': ['rank', 'status', 'uid']}),
        ]
        if obj is None:
            self.fieldsets = self.add_fieldsets
        else:
            self.readonly_fields = ['get_name', 'get_awards']
            self.fieldsets = self.change_fieldsets
        return super(PersonnelAdmin, self).get_formsets(request, obj)
    search_fields = ['psin__fname', 'psin__lname']
    list_display = ('get_fname', 'get_lname', 'get_sin')
    list_filter = ['status','rank']
    inlines = [SuperviseeInline, AuthorizedInline]
    class Media:
        js = ("/static/js/hide_mypersonnel_info.js",)


class PersonnelInline(admin.TabularInline):
    list_select_related = True

    model = Personnel
    verbose_name_plural = 'Members'
    extra = 0
    def get_queryset(self, request):
        return super(PersonnelInline, self).get_queryset(request).select_related()
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    class Media:
        js = ("/static/js/disable_inline_info.js",)

class EquipmentInline(admin.TabularInline):
    model = Equipment
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
    list_select_related = True
    fieldsets = [
        ('Unit Information', {'fields': ['uid', 'uname', 'type', 'bid', 'cid', 'commander_sin']})]
    search_fields = ['uname']
    list_display = ('uname', 'type', 'get_bname', 'get_cname', 'uid')
    list_filter = ['type']
    inlines = [PersonnelInline]
    def get_queryset(self, request):
        return super(UnitAdmin, self).get_queryset(request).select_related()
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
    inlines = [UnitInline, EquipmentInline]
    class Media:
        js = ("/static/js/hide_mybase_info.js",)



class AwardAdmin(admin.ModelAdmin):
    search_fields = ['aname']
    list_display = ('aname', 'code')
    class Media:
        js = ("/static/js/disable_inline_info.js",)


class OperationInline(admin.TabularInline):
    model = Operations
    extra = 0
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    class Media:
        js = ("/static/js/disable_inline_info.js",)


class ConflictAdmin(admin.ModelAdmin):
    search_fields = ['cname']
    list_display = ('cname', 'status', 'start_date', 'cid')
    list_filter = ['status']
    inlines = [UnitInline, OperationInline]
    class Media:
        js = ("/static/js/disable_inline_info.js",)

class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['ename']
    list_display = ('ename', 'type', 'status', 'get_bname', 'get_cname', 'serialno')
    list_filter = ['type', 'status']
    inlines = [AuthorizedInline]
    class Media:
        js = ("/static/js/disable_inline_info.js",)


class OperationsAdmin(admin.ModelAdmin):
    exclude = ['id']
    search_fields = ['oname']
    list_display = ('oname', 'type', 'get_cname')
    list_filter = ['type']
    class Media:
        js = ("/static/js/disable_inline_info.js",)


class VeteranAdmin(admin.ModelAdmin):
    search_fields = ['fname', 'lname']
    list_display = ('get_fname', 'get_lname', 'end_date', 'vsin')
    def has_add_permission(self, request, obj=None):
        return False
    class Media:
        js = ("/static/js/disable_inline_info.js",)

admin.site.register(Person, PersonAdmin)
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Conflict, ConflictAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Operations, OperationsAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Veteran, VeteranAdmin)
