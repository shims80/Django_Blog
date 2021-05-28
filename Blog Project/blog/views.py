from django.shortcuts import render

posts = [
    {
        'author' :'shimon shitrit',
        'title': 'Blog Post 1', 
        'content' : 'first post content',
        'date_posted' : 'Jun 5 ,1980',
    },
    {
        'author' :'leo my dog',
        'title': 'Blog Post ', 
        'content' : 'second post content',
        'date_posted' : 'March 1 ,2012',
    }
]
# Create your views here.

def home(request):
    context = {
        'posts':posts
    }
    return render (request,'blog/home.html',context)

def about(request):
    return render (request,'blog/about.html',{'title':'About'})

