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
    score = request.GET.get('score')
    writer = request.GET.get('writer')

    Review.objects.create(title=title, content=content, score=score, writer=writer)

    return redirect('movie:details')

def detail(request, review_pk):

    review = Review.objects.get(id=review_pk)

    context = {
        'review': review
    }
    
    return render(request, 'movie/detail.html', context)

def details(request):

    reviews = Review.objects.all()

    context = {
        'reviews' : reviews
    }

    return render(request, 'movie/details.html', context)

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
    score = request.GET.get('score')

    review.title = title
    review.content = content
    review.score = score
    review.save()
   
    return redirect('movie:details')

def delete(request, review_pk):
    review = Review.objects.get(id=review_pk)
    review.delete()

    return redirect('movie:details')