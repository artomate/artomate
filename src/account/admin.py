from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, KycInfo


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


def Verify(modeladmin, request, queryset):
    queryset.update(kycstatus=3)


def reject(modeladmin, request, queryset):
    queryset.update(kycstatus=4)


class KycAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'dob', 'mobile', 'idprooffront', 'idproofback', 'kycstatus', 'userid', 'username')
    actions = [Verify, reject]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(KycInfo, KycAdmin)
