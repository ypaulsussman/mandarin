from django.shortcuts import render
from .models import Chengyu

import os
import boto3
from dotenv import load_dotenv
load_dotenv()


def index(request):
    context = {
        'most_common_chengyus': Chengyu.objects.exclude(chengyu_translation='').order_by('z_rarity')[:5],
    }
    return render(request, 'fourchar/index.html', context)


def search(request):
    query_string = request.GET.get('q')
    matching_chengyus = Chengyu.objects.filter(
        chengyu_text__contains=query_string
    )
    decorated_chengyus = []
    client = boto3.client(
        'translate',
        aws_access_key_id=os.environ["ACCESS_KEY"],
        aws_secret_access_key=os.environ["SECRET_KEY"],
    )

    for chengyu in matching_chengyus:
        response = client.translate_text(
            Text=chengyu.chengyu_text,
            SourceLanguageCode='zh',
            TargetLanguageCode='en'
        )
        chengyu.chengyu_translation = response['TranslatedText']
        decorated_chengyus.append(chengyu)

    return render(
        request,
        'fourchar/search.html',
        {
            'matching_chengyus': decorated_chengyus,
            'query': query_string
        }
    )
