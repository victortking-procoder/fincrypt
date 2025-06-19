import re
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def blog_list(request):
    articles = Article.objects.order_by('sequence')
    return render(request, 'blog/blog_list.html', {'articles': articles})

def article_detail(request, sequence):
    if sequence > 10:
        return redirect('article', sequence=1)

    # 🔁 Redirect to ad-wait if on article 10 and 'ads_clicked' is NOT true
    if sequence == 10 and request.GET.get('ads_clicked') != 'true':
        return redirect('ad_wait')

    article = get_object_or_404(Article, sequence=sequence)
    next_article = sequence + 1 if sequence < 10 else None
    show_code = (sequence == 10 and request.GET.get('ads_clicked') == 'true')

    # 🔸 Process article content into paragraphs
    paragraphs = re.split(r'\n{2,}', article.content.strip()) if article.content else []

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'next_sequence': next_article,
        'show_code': show_code,
        'code': 'X9-KLM-2025' if show_code else None,
        'sequence': sequence,
        'paragraphs': paragraphs,
    })

def ad_wait(request):
    return render(request, 'blog/ad_wait.html', {'redirect_to': '/article/10/?ads_clicked=true'})
