from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import UserInfo
from users.models import ReservedItems


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


@admin.register(ReservedItems)
class ReservedItemsAdmin(admin.ModelAdmin):
    def name(self, obj):
        user = User.objects.get(id=obj.user.id)
        return user.first_name + " " + user.last_name

    def reservation_date_(self, obj):
        reserve = ReservedItems.objects.get(id=obj.id)
        data = reserve.reservation_date
        return data.strftime("%d/%m/%Y")

    def pickup_date_(self, obj):
        reserve = ReservedItems.objects.get(id=obj.id)
        data = reserve.pickup_date
        return data.strftime("%d/%m/%Y")

    list_display = [
        "id",
        "name",
        "item",
        "items_quantity",
        "reservation_date_",
        "pickup_date_",
    ]
    ordering = ["id"]
    search_fields = ["id"]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
