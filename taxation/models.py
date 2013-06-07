# -*- coding: utf-8 -*-
from django.db import models


class ParentModel(models.Model):
    class Meta:
        abstract = True

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields


class Description(models.Model):
    afs = models.PositiveSmallIntegerField(verbose_name=u'АФС №')
    region = models.CharField(max_length=50, verbose_name=u'Респбулика Область Край')
    administrative_region = models.CharField(max_length=50, verbose_name=u'Административный район')
    forestry = models.CharField(max_length=50, verbose_name=u'Лесничество')
    purpose = models.CharField(max_length=50, verbose_name=u'Целевое назначение лесов')
    protection_category = models.CharField(max_length=50, verbose_name=u'Шифр категории защитных лесов')
    rent = models.CharField(max_length=50, verbose_name=u'Аренда')
    relief = models.CharField(max_length=50, verbose_name=u'Рельеф')
    recreation_area = models.CharField(max_length=50, verbose_name=u'Рекреационная зона')
    performer = models.CharField(max_length=50, verbose_name=u'Исполнитель')
    responsible = models.CharField(max_length=50, verbose_name=u'Ответственный')
    date = models.DateField(verbose_name=u'Дата заполнения')

    class Meta:
        ordering = ['-id']

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
            field.type = str(type(field))
        return fields[1:]

    def get_absolute_url(self):
        return "/description/%i/" % self.id

    def add_card_url(self):
        return "/description/%d/card/add/" % self.id

    def edit_url(self):
        return "/description/%d/edit/" % self.id

    def delete_url(self):
        return "/description/%d/delete" % self.id


class Card(models.Model):
    description = models.ForeignKey(Description)
    number_quarter = models.PositiveSmallIntegerField(verbose_name=u'№ квартала')
    way = models.CharField(max_length=50, verbose_name=u'Ход')
    point = models.CharField(max_length=50, verbose_name=u'Пункт таксации')
    distance = models.CharField(max_length=50, verbose_name=u'Расстояние')

    class Meta:
        ordering = ['-id']

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]

    def get_absolute_url(self):
        return "/description/%d/card/%d/" % (self.description.id, self.id)

    def edit_url(self):
        return "/description/%d/card/%d/edit" % (self.description.id, self.id)

    def delete_url(self):
        return "/description/%d/card/%d/delete" % (self.description.id, self.id)


class Table1(models.Model):
    card = models.OneToOneField(Card)
    section_number = models.PositiveIntegerField(verbose_name=u'№ Выдела')
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Площадь, га')
    land_category = models.PositiveSmallIntegerField(verbose_name=u'Категория земель')
    long_term_use = models.CharField(max_length=50, verbose_name=u'Долгосрочное пользование')
    special_protection_area = models.CharField(max_length=50, verbose_name=u'Особо защитный участок')
    slope_exposure = models.CharField(max_length=50, verbose_name=u'Экспозиция склона')
    slope_steepness = models.CharField(max_length=50, verbose_name=u'Крутизна склона')
    altitude = models.IntegerField(verbose_name=u'Высота над уровнем моря')
    erosion_view = models.CharField(max_length=50, verbose_name=u'Вид эрозии')
    erosion_degree = models.CharField(max_length=50, verbose_name=u'Степень эрозии')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]


class Table2(models.Model):
    card = models.OneToOneField(Card)
    first_event = models.CharField(max_length=50, verbose_name=u'1-ое')
    first_event_degree = models.PositiveSmallIntegerField(verbose_name=u'%')
    first_event_number_rtk = models.CharField(max_length=50, verbose_name=u'№ РТК')
    second_event = models.CharField(max_length=50, verbose_name=u'2-ое')
    second_event_number_rtk = models.CharField(max_length=50, verbose_name=u'№ РТК')
    third_event = models.CharField(max_length=50, verbose_name=u'3-ое')
    third_event_number_rtk = models.CharField(max_length=50, verbose_name=u'№ РТК')
    target_species = models.CharField(max_length=50, verbose_name=u'Целевая порода')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]


class Table3(models.Model):
    card = models.OneToOneField(Card)
    species = models.CharField(max_length=50, verbose_name=u'Порода')
    bondability = models.CharField(max_length=50, verbose_name=u'Бонитет')
    wood_type = models.CharField(max_length=50, verbose_name=u'Тип леса')
    TLU = models.CharField(max_length=50, verbose_name=u'ТЛУ')
    year_cutting = models.PositiveSmallIntegerField(verbose_name=u'Год вырубки')
    number_stumps = models.PositiveIntegerField(verbose_name=u'Количество пней, шт/га')
    number_stumps_pine = models.PositiveIntegerField(verbose_name=u'Количество пней (Сосны), шт/га')
    diameter_stumps = models.PositiveIntegerField(verbose_name=u'Диаметр пней')
    type_cutting = models.CharField(max_length=50, verbose_name=u'Тип вырубки')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]


class Table4(models.Model):
    card = models.OneToOneField(Card)
    clutter_general = models.CharField(max_length=50, verbose_name=u'Общая захламленность')
    clutter_liquidity = models.CharField(max_length=50, verbose_name=u'Ликвидная захламленность')
    old_deadwood = models.CharField(max_length=50, verbose_name=u'Старый сухостой')
    text_record = models.CharField(max_length=250, verbose_name=u'Текстовая запись')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]


class Table31(models.Model):
    card = models.OneToOneField(Card)
    undergrowth_count = models.PositiveSmallIntegerField(verbose_name=u'Количество, тыс. шт.')
    undergrowth_h = models.PositiveSmallIntegerField(verbose_name=u'H, м')
    undergrowth_a = models.PositiveSmallIntegerField(verbose_name=u'A, лет')
    undergrowth_ratio_1 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u'Коэффициент')
    undergrowth_species_1 = models.CharField(max_length=50, verbose_name=u'Порода')
    undergrowth_ratio_2 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u'Коэффициент')
    undergrowth_species_2 = models.CharField(max_length=50, verbose_name=u'Порода')
    undergrowth_ratio_3 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=u'Коэффициент')
    undergrowth_species_3 = models.CharField(max_length=50, verbose_name=u'Порода')
    rating = models.CharField(max_length=50, verbose_name=u'Оценка')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]


class Table32(models.Model):
    card = models.OneToOneField(Card)
    underbrush = models.CharField(max_length=50, verbose_name=u'Густота')
    underbrush_species_1 = models.CharField(max_length=50, verbose_name=u'Порода')
    underbrush_species_2 = models.CharField(max_length=50, verbose_name=u'Порода')
    underbrush_species_3 = models.CharField(max_length=50, verbose_name=u'Порода')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]


class Stage(models.Model):
    card = models.ForeignKey(Card)
    stage = models.PositiveSmallIntegerField(verbose_name=u'Ярус')
    composition_ratio = models.PositiveSmallIntegerField(verbose_name=u'Коэффициент')
    composition_species = models.CharField(max_length=50, verbose_name=u'Порода')
    a = models.PositiveSmallIntegerField(verbose_name=u'A, лет')
    h = models.PositiveSmallIntegerField(verbose_name=u'H, м')
    d = models.PositiveSmallIntegerField(verbose_name=u'D, см')
    class_merchantability = models.CharField(max_length=50, verbose_name=u'Класс товарности')
    origin = models.CharField(max_length=50, verbose_name=u'Происхождение')
    completeness = models.CharField(max_length=50, verbose_name=u'Полнота')
    sum_g = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u'Σg')
    stock = models.PositiveIntegerField(verbose_name=u'Запас м³/га')

    def fields(self):
        fields = self._meta.fields
        for field in fields:
            field.value = getattr(self, field.name)
        return fields[2:]