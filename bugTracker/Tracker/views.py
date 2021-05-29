from django.shortcuts import render


posts = [
    {
        'author':  'Corey',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'August 21',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'August 22',
       }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'Tracker/home.html', context)


def about(request):
    return render(request, 'Tracker/about.html')
