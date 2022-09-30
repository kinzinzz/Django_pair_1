from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def index(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }
    return render(request, 'movie/index.html', context)

def create(request):

    # title = request.GET.get('title')
    # content = request.GET.get('content')
    # Review.objects.create(title=title, content=content)

    return render(request, 'movie/create.html')

def write(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)

    return redirect('movie:index')

def detail(request, review_pk):

    review = Review.objects.get(id=review_pk)

    context = {
        'review': review
    }
    
    return render(request, 'movie/detail.html', context)

def edit(request, review_pk):
    review = Review.objects.get(id=review_pk)

    context = {
        'review': review,
    }

    return render (request, 'movie/edit.html',context)

def update(request, review_pk):
    
    review = Review.objects.get(id=review_pk)
    title = request.GET.get('title')
    content = request.GET.get('content')

    review.title = title
    review.content = content
    review.save()
   
    return redirect('movie:index')

def delete(request, review_pk):
    review = Review.objects.get(id=review_pk)
    review.delete()

    return redirect('movie:index')