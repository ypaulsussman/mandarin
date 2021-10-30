from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render

from .models import Chengyu


def index(request):
    context = {
        'most_common_chengyus': Chengyu.objects.exclude(chengyu_translation='').order_by('z_rarity')[:5],
    }
    return render(request, 'fourchar/index.html', context)


def search(request, query):
    return render(
        request,
        'fourchar/search.html',
        {
            'matching_chengyus': Chengyu.objects.filter(chengyu_text__contains=query),
            'query': query
        }
    )
