from django.contrib import admin
from .models import Users, Spa_items, Orders

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_id', 'tg_name')

class Spa_itemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_desc', 'item_price', 'item_photo')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'spa_item', 'created_dt', 'last_updated_dt', 'status', 'start_time')


admin.site.register(Users, UsersAdmin)
admin.site.register(Spa_items, Spa_itemsAdmin)
admin.site.register(Orders, OrdersAdmin)
