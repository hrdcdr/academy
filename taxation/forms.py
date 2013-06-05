from models import Description, Card, Stage, Table1, Table2, Table3, Table4, Table31, Table32
from django.forms import ModelForm, forms


class DescriptionForm(ModelForm):
    class Meta:
        model = Description


class CardForm(ModelForm):
    class Meta:
        model = Card
        exclude = ('description',)


class Table1Form(ModelForm):
    class Meta:
        model = Table1
        exclude = ('card',)


class Table2Form(ModelForm):
    class Meta:
        model = Table2
        exclude = ('card',)


class Table3Form(ModelForm):
    class Meta:
        model = Table3
        exclude = ('card',)


class Table4Form(ModelForm):
    class Meta:
        model = Table4
        exclude = ('card',)


class Table31Form(ModelForm):
    class Meta:
        model = Table31
        exclude = ('card',)


class Table32Form(ModelForm):
    class Meta:
        model = Table32
        exclude = ('card',)


class StageForm(ModelForm):
    class Meta:
        model = Stage
