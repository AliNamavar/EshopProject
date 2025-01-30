from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from site_module.models import site_banner
from .models import Article, ArticleCategory, ArticleComments


# Create your views here.

# class ArticleView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         return render(request, 'article_module/article_page.html', {
#             'articles': articles
#         })

class ArticleListView(ListView):
    model = Article
    paginate_by = 1
    template_name = 'article_module/article_page.html'

    # context_object_name = 'articles'
    # return kardane maqaleye filter shode dar component
    def get_queryset(self):
        query = super(ArticleListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detail_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query


    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        article: Article = kwargs.get('object')
        context['comment'] = (ArticleComments.objects.filter(article_id=article.id, parent=None)
                              .prefetch_related('articlecomments_set').order_by('-created_date'))
        context['comments_count'] = ArticleComments.objects.filter(article_id=article.id).count()
        context['banners'] = site_banner.objects.filter(is_active=True, position__iexact=site_banner.site_banner_position.article_detail)
        return context


def article_category_component(request):
    main_categorys = ArticleCategory.objects.filter(is_active=True, parent_id=None).prefetch_related('articlecategory_set')
    context = {
        'main_categorys': main_categorys
    }
    return render(request, 'component/article_category_component.html', context)


def article_comments(request):
    if request.user.is_authenticated:
        article_comment = request.GET.get('article_comments')
        article_id = request.GET.get('article_id')
        article_parent_id = request.GET.get('parent_id')
        print(article_id, article_comment)
        new_article_comment = ArticleComments(article_id=article_id, text=article_comment, author_id=request.user.id, parent_id=article_parent_id)
        new_article_comment.save()
        context = {
            'comment': ArticleComments.objects.filter(article_id=article_id, parent=None).prefetch_related('articlecomments_set').order_by('-created_date'),
            'comments_count': ArticleComments.objects.filter(article_id=article_id).count()
        }
        return render(request, 'includes/article_comment_component.html', context)
    return HttpResponse('Comment received successfully!')
