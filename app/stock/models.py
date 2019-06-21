from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    code = models.IntegerField(_('Code'))
    name = models.CharField(_('Name'), max_length=200)
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE)
    unit_price = models.DecimalField(
        _('Unit Price'),
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        default=None
    )
    stock = models.PositiveSmallIntegerField(
        _('Stock'), default=0)

    class Meta:
        verbose_name = _('Article')

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse_lazy('stock:article_list')
