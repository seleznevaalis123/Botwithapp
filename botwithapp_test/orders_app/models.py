from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.db import models

class Users(models.Model):
    '''Users'''

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    tg_id = models.IntegerField(verbose_name='tg id')
    tg_name = models.TextField(verbose_name='name tg')

    def __str__(self):
        return self.tg_name


class Spa_items(models.Model):
    '''Spaitems'''

    class Meta:
        db_table = 'spa_items'
        verbose_name = 'spa item'
        verbose_name_plural = 'spa items'

    item_name = models.TextField(verbose_name='Spa item name')
    item_desc = models.TextField(verbose_name='Spa item desc')
    item_price = models.IntegerField(verbose_name='Spa item price')
    item_photo = models.ImageField(upload_to='photo/', verbose_name='Spa item photo')

    def __str__(self):
        return f'{self.item_name}'


class Orders(models.Model):
    '''Orders'''

    Order_states = [
        ('NEW', 'new'),
        ('IN_PROGRESS', 'in_progress'),
        ('DONE', 'done'), ]
    class Meta:
        db_table = 'user_orders'
        verbose_name = 'order'
        verbose_name_plural = 'order'

    user_id = models.ForeignKey(Users, on_delete=models.RESTRICT, verbose_name='User')
    spa_item = models.ForeignKey(Spa_items, verbose_name='Spa item', on_delete=models.RESTRICT)
    created_dt = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    last_updated_dt = models.DateTimeField(verbose_name='Last update', blank=True, null=True)
    status = models.CharField(verbose_name='State', max_length=20, choices=Order_states)
    start_time = models.TimeField(verbose_name='Start time')

    def __str__(self):
        return self.status



