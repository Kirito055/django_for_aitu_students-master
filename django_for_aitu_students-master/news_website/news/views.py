from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import * # do not forget to import your models!
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
def index(request):
    # return HttpResponse("This is main page of our project") # old version

    # ordering by date descending using article_date column
    latest_articles = Article.objects.order_by('-article_date')

    # returning result with render function (request, template, context)
    return render(request, "news/index.html", {"latest_articles":latest_articles})

def get_article_by_id(request, id):
    # get_object_or_404 usage

    article = get_object_or_404(Article, pk=id)
    return render(request, "news/article.html", {"article":article})

def get_user_by_id(request, id):
    # get_object_or_404 usage

    user = get_object_or_404(User, pk=id)
    return render(request, "users/profile.html", {"user": user})

    # below is the old code
    # try:
    #     # print(request, id) # this is to see that everything is coming here
    #     article = Article.objects.get(pk=id)
    # except:
    #     raise Http404(f"No such article with id #{id}")
    #     # return HttpResponse(f"No such article with id #{id}")
    # return HttpResponse(f"Article text with id {id}: <br> {article.article_text}")

def search_by_article_text(request, text):
    search_result = list(Article.objects.filter(article_text__contains=text).values_list("article_text"))
    print(search_result)
    try:
        articles = ""
        for i in search_result:
            articles += f"<h3>#{search_result.index(i)+1}:{str(*i)} </h3><br>"
        print(articles)
        return HttpResponse(f"<h2>This is the result of search: </h2><br> {articles}")
    except Exception as e:
        print(e)
        return HttpResponse(f'No such article with text: {text}')

def articles_archive(request):
    query = list(Article.objects.all())
    all_articles = ""
    if len(query)>0:
        for i in query:
            all_articles += i.article_text + "<br>"
        return HttpResponse(f"This is archive of all articles: <br> {all_articles}")
    else:
        return HttpResponse("There are no articles yet")

def articles_comments(request):
    pass # will be implemented in later development phases

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'