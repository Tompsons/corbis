from django.forms import ModelForm, NumberInput, Select
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _

from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'code': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Code'),
                },
            ),
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name'),
                },
            ),
            'category': Select(
                attrs={
                    'class': 'selectpicker',
                },
            ),
            'unit_price': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Unit Price'),
                },
            ),
            'stock': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Stock'),
                },
            ),
        }
