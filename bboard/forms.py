from django.core.exceptions import ValidationError
from django.forms import ModelForm, modelform_factory, DecimalField
from django import forms
from django.forms.widgets import Select
from django.core import validators
from bboard.models import Bb, Rubric, IceCream


# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')


# BbForm = modelform_factory(Bb,
#                            fields=('title', 'content', 'price', 'rubric'),
#                            labels={'title': 'Название товара'},
#                            help_texts={'rubric': 'He забудьте выбрать рубрику!'},
#                            field_classes={'price': DecimalField},
#                            widgets={'rubric': Select(attrs={'size': 8})})


# class BbForm(ModelForm) :
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels = {'title': 'Название товара'}
#         help_texts = {'rubric': 'He забудьте задать рубрику!'}
#         field_classes = {'price': DecimalField}
#         widgets = {'rubric': Select(attrs={'size': 8})}


class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара',
                            validators=[validators.RegexValidator(regex='^.{4,}$')],
                            error_messages={'invalid': 'Слишком короткое название товара!'})

    # content = forms.CharField(label='Описание',
    #                           widget=forms.widgets.Textarea(),
    #                           validators=[validators.RegexValidator(regex='^.{30,}$')],   # lesson_26_hw
    #                     error_messages={'invalid': 'Описание товара должно быть больше 30 символов!'})  # lesson_26_hw
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                    label='Рубрика',
                                    help_text='He забудьте задать рубрику!',
                                    widget=forms.widgets.Select(attrs={'size': 8}))

    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допускается! Лучше продавай плотины')
        return val

    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('Укажите описание')
        if self.cleaned_data['price'] <= 0:
            errors['price'] = ValidationError('Укажите положительное значение цены')
        if errors:
            raise ValidationError(errors)

    class Meta:
        model = Bb
        fields = ('title', 'price', 'rubric')  # lesson_25_hw убрал content


# class BbForm(forms.ModelForm):
#     price = forms.DecimalField(label='Цена', decimal_places=2)
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
#                                     label='Рубрика',
#                                     help_text='He забудьте задать рубрику!',
#                                     widget=forms.widgets.Select(attrs={'size': 8}))
#
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels = {'title': 'Название товара'}


class IceCreamForm(ModelForm):  # lesson_25_hw
    class Meta:
        model = IceCream
        fields = ('title', 'content', 'price', 'quantity', 'compound')
