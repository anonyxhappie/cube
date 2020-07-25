from django.contrib import admin

from .models import Event, EventRules


class EventAdmin(admin.ModelAdmin):
    actions = None
    fieldsets = [
        (None, {'fields':()}), 
        ]
    search_fields = ['={}'.format(field.name) for field in Event._meta.get_fields()]
    list_display = [field.name for field in Event._meta.get_fields()]

    def __init__(self, *args, **kwargs):
        super(EventAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = None

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'List of events'}
        return super(EventAdmin, self).changelist_view(request, extra_context=extra_context)


class EventRulesAdmin(admin.ModelAdmin):
    actions = None
    search_fields = ['={}'.format(field.name) for field in EventRules._meta.get_fields()]
    list_display = [field.name for field in EventRules._meta.get_fields()]

    def __init__(self, *args, **kwargs):
        super(EventRulesAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('rule_name',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'List of event rules'}
        return super(EventRulesAdmin, self).changelist_view(request, extra_context=extra_context)




admin.site.register(Event, EventAdmin)
admin.site.register(EventRules, EventRulesAdmin)