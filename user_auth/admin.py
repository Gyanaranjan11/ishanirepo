from django.contrib import admin
from user_auth.models import UserModel

# Register your models here.
class AdminUserModel(admin.ModelAdmin):
    list_display = ['name', 'email', 'mob_no', 'password', 'gender', 'email_verify',
                    'status', 'photo', 'created_date', 'modify_date', 'deleted_date','mob_no_verify']
admin.site.register(UserModel, AdminUserModel)
