from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import UserInfo


# Define an inline admin descriptor for UserInfo model
# which acts a bit like a singleton
class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name = "Informação adicional"
    verbose_name_plural = "Informações adicionais"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    def phone_number(self, obj):
        user_info = UserInfo.objects.get(user=obj.id)
        if hasattr(user_info, "phone_number"):
            return user_info.phone_number
        else:
            return "-"

    phone_number.short_description = "Telefone"
    list_display = BaseUserAdmin.list_display + ("phone_number",)
    inlines = [UserInfoInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
