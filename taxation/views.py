# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from models import Description, Card, Stage, Table1, Table2, Table3, Table4, Table31, Table32
from forms import DescriptionForm, CardForm, StageForm, Table1Form, Table2Form, Table3Form, Table4Form, Table31Form, Table32Form
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from datetime import datetime


@login_required
def index(request):
    i = 0
    kwargs = {}
    cs = request.POST.getlist('condition')
    fs = request.POST.getlist('filter')
    for c in cs:
        if c == 'date__exact' or c == 'date__lte' or c == 'date__gte':
            kwargs[c] = datetime.strptime(fs[i], '%d.%m.%Y')
        else:
            kwargs[c] = fs[i]
            i += 1
    descriptions_list = Description.objects.filter(**kwargs)
    paginator = Paginator(descriptions_list, 5)
    page = request.GET.get('page')
    try:
        descriptions = paginator.page(page)
    except PageNotAnInteger:
        descriptions = paginator.page(1)
    except EmptyPage:
        descriptions = paginator.page(paginator.num_pages)
    content = {
        'Description': Description,
        'descriptions': descriptions,
    }
    return render(request, 'index.html', content)


@login_required
def description_view(request, did):
    description = Description.objects.get(pk=did)
    cards = Card.objects.filter(description=description)
    content = {
        'description': description,
        'cards': cards,
    }
    content.update(csrf(request))
    return render(request, 'description_view.html', content)


@login_required
def card_view(request, did, cid):
    description = Description.objects.get(pk=did)
    card = Card.objects.get(pk=cid)
    table1 = Table1.objects.get(card=card)
    table2 = Table2.objects.get(card=card)
    table3 = Table3.objects.get(card=card)
    table4 = Table4.objects.get(card=card)
    table31 = Table31.objects.get(card=card)
    table32 = Table32.objects.get(card=card)
    stages = Stage.objects.filter(card=card)
    content = {
        'description': description,
        'card': card,
        'table1': table1,
        'table2': table2,
        'table3': table3,
        'table4': table4,
        'table31': table31,
        'table32': table32,
        'stages': stages,
    }
    return render(request, 'card_view.html', content)


@login_required
def description_add(request):
    if request.method == 'POST':
        descriptionform = DescriptionForm(request.POST)
        if descriptionform.is_valid():
            description = descriptionform.save()
            return HttpResponseRedirect(description.get_absolute_url())
    else:
        descriptionform = DescriptionForm()
    content = {
        'descriptionform': descriptionform,
    }
    content.update(csrf(request))
    return render(request, 'description_edit.html', content)


@login_required
def description_edit(request, did):
    description = Description.objects.get(pk=did)
    if request.method == 'POST':
        descriptionform = DescriptionForm(request.POST, instance=description)
        if descriptionform.is_valid():
            description = descriptionform.save()
            return HttpResponseRedirect(description.get_absolute_url())
    else:
        descriptionform = DescriptionForm(instance=description)
    content = {
        'description': description,
        'descriptionform': descriptionform,
    }
    content.update(csrf(request))
    return render(request, 'description_edit.html', content)


@login_required
def card_add(request, did):
    description = Description.objects.get(pk=did)
    StageFormset = inlineformset_factory(Card, Stage, form=StageForm, extra=1)
    if request.method == 'POST':
        cardform = CardForm(request.POST)
        table1form = Table1Form(request.POST)
        table2form = Table2Form(request.POST)
        table3form = Table3Form(request.POST)
        table4form = Table4Form(request.POST)
        table31form = Table31Form(request.POST)
        table32form = Table32Form(request.POST)
        stageformset = StageFormset(request.POST)
        if cardform.is_valid() and table1form.is_valid() and table2form.is_valid() and table3form.is_valid() and table4form.is_valid() and table31form.is_valid() and table32form.is_valid():
            card = cardform.save(commit=False)
            card.description = description
            card.save()
            table1 = table1form.save(commit=False)
            table1.card = card
            table1.save()
            table2 = table2form.save(commit=False)
            table2.card = card
            table2.save()
            table3 = table3form.save(commit=False)
            table3.card = card
            table3.save()
            table4 = table4form.save(commit=False)
            table4.card = card
            table4.save()
            table31 = table31form.save(commit=False)
            table31.card = card
            table31.save()
            table32 = table32form.save(commit=False)
            table32.card = card
            table32.save()
            stageformset = StageFormset(request.POST, instance=card)
            if stageformset.is_valid():
                stageformset.save()
            return HttpResponseRedirect(card.get_absolute_url())
    else:
        cardform = CardForm()
        table1form = Table1Form()
        table2form = Table2Form()
        table3form = Table3Form()
        table4form = Table4Form()
        table31form = Table31Form()
        table32form = Table32Form()
        stageformset = StageFormset()
    content = {
        'description': description,
        'cardform': cardform,
        'table1form': table1form,
        'table2form': table2form,
        'table3form': table3form,
        'table4form': table4form,
        'table31form': table31form,
        'table32form': table32form,
        'stageformset': stageformset,
    }
    content.update(csrf(request))
    return render(request, 'card_edit.html', content)


@login_required
def card_edit(request, did, cid):
    description = Description.objects.get(pk=did)
    card = Card.objects.get(pk=cid)
    table1 = Table1.objects.get(card=card)
    table2 = Table2.objects.get(card=card)
    table3 = Table3.objects.get(card=card)
    table4 = Table4.objects.get(card=card)
    table31 = Table31.objects.get(card=card)
    table32 = Table32.objects.get(card=card)
    StageFormset = inlineformset_factory(Card, Stage, form=StageForm, extra=1)
    if request.method == 'POST':
        cardform = CardForm(request.POST, instance=card)
        table1form = Table1Form(request.POST, instance=table1)
        table2form = Table2Form(request.POST, instance=table2)
        table3form = Table3Form(request.POST, instance=table3)
        table4form = Table4Form(request.POST, instance=table4)
        table31form = Table31Form(request.POST, instance=table31)
        table32form = Table32Form(request.POST, instance=table32)
        stageformset = StageFormset(request.POST, instance=card)
        if cardform.is_valid() and table1form.is_valid() and table2form.is_valid() and table3form.is_valid() and table4form.is_valid() and table31form.is_valid() and table32form.is_valid() and stageformset.is_valid():
            cardform.save()
            table1form.save()
            table2form.save()
            table3form.save()
            table4form.save()
            table31form.save()
            table32form.save()
            stageformset.save()
            return HttpResponseRedirect(card.get_absolute_url())
    else:
        cardform = CardForm(instance=card)
        table1form = Table1Form(instance=table1)
        table2form = Table2Form(instance=table2)
        table3form = Table3Form(instance=table3)
        table4form = Table4Form(instance=table4)
        table31form = Table31Form(instance=table31)
        table32form = Table32Form(instance=table32)
        stageformset = StageFormset(instance=card)
    content = {
        'description': description,
        'card': card,
        'cardform': cardform,
        'table1form': table1form,
        'table2form': table2form,
        'table3form': table3form,
        'table4form': table4form,
        'table31form': table31form,
        'table32form': table32form,
        'stageformset': stageformset,
    }
    content.update(csrf(request))
    return render(request, 'card_edit.html', content)


@login_required
def description_delete(request, did):
    description = Description.objects.get(pk=did)
    description.delete()
    return HttpResponseRedirect('/')


@login_required
def card_delete(request, did, cid):
    description = Description.objects.get(pk=did)
    card = Card.objects.get(pk=cid)
    card.delete()
    return HttpResponseRedirect(description.get_absolute_url())