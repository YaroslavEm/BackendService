from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import SearchForm
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = request.POST.get('keyword')
            qs = Article.objects.filter(title__iexact=keyword)
            if qs:
                return redirect('article', keyword.replace(' ', '_').lower())
    else:
        form = SearchForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/home.html', context=context)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    lookup_field = 'title'

    def get_queryset(self):
        title = self.kwargs.get('title').replace('_', ' ')
        if not title:
            return Article.objects.all()
        return Article.objects.filter(title__iexact=title)
