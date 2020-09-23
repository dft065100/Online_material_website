from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from django.utils.safestring import mark_safe

# Create your views here.
def article_list(request):
    articles = ArticlePost.objects.all()
    context = { 'articles': articles }
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article_list = ArticlePost.objects.all()
    particle_list = article_list.filter(particle__isnull = True)
    article = ArticlePost.objects.get(id=id)
    context = { 'article': article, 'particle_list': particle_list }
    return render(request, 'article/detail.html', context)

def ajax_article_list(request):
    data = request.POST
    id = data.get("id")
    articles = ArticlePost.objects.all()
    subarticle_list = articles.filter(particle__exact=id)
    json_data = serialize('json', subarticle_list)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)

def ajax_article_detail(request):
    data = request.POST
    id = data.get("id")
    articles = ArticlePost.objects.all()
    article = articles.filter(id__exact=id)
    json_data = serialize('json', article)
    json_data = json.loads(json_data)
    return JsonResponse(json_data, safe=False)
