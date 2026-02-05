from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ['owner']
    verbose_name = "Собственник(и)"
    extra = 0


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address',]
    readonly_fields = ['construction_year']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
    ]
    list_editable = ['new_building']
    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony',
    ]
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]
admin.site.register(Flat, FlatAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['snitch', 'flat']

admin.site.register(Complaint, ComplaintAdmin)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat']

admin.site.register(Owner, OwnerAdmin)

