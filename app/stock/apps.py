from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class StockConfig(AppConfig):
    name = 'stock'
    verbose_name = ugettext_lazy('Stock Management Console')
