from django.shortcuts import render
from myapp.models import ArticleModel as A
# Create your views here.

def home_view(request):
    return render(request,'home.html')

def form_view(request):
    submited = False
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        author = request.POST.get('author')
        date = request.POST.get('date')
        A.objects.create(title = title,description = desc,author = author,date = date)
        submited = True

    return render(request,'form.html',{'submited':submited})

def all_articles(request):
    all_data = A.objects.all()
    return render(request,'all_articles.html',{"all_data":all_data})

def specific_view(request,id):
    data = A.objects.get(id = id)
    return render(request,'specific.html',{'data':data})