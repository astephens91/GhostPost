from django.shortcuts import render, HttpResponseRedirect, reverse
from GhostProject.models import Post
from GhostProject.forms import AddPost


def index(request):
    html = "index.html"

    posts = Post.objects.all().order_by("-post_date")

    return render(request, html, {'data': posts})


def boasts(request):
    html = "boasts.html"

    posts = Post.objects.all().filter(is_boast=True).order_by("-post_date")

    return render(request, html, {'data': posts})


def roasts(request):
    html = "roasts.html"

    posts = Post.objects.all().filter(is_boast=False).order_by("-post_date")

    return render(request, html, {'data': posts})


def addpostview(request):
    html = 'generic_form.html'

    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Post.objects.create(
                is_boast=data['is_boast'],
                content=data['content'],
                author=data['author'],
            )
        return HttpResponseRedirect(reverse('homepage'))
    
    form = AddPost()
    return render(request, html, {'form': form})

def upvoting(request, id):
    html = "index.html"

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    
    post.up_votes += 1
    post.net_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvoting(request, id):
    html = "index.html"

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))

    post.down_vote += 1
    post.net_votes -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def netvotes(request):
    html = "netvotes.html"

    posts = Post.objects.all().order_by("-net_votes")

    return render(request, html, {'data': posts})


def delete_post(request, id):

    post_to_delete = Post.objects.get(id=id)

    post_to_delete.delete()

    return HttpResponseRedirect(reverse('homepage'))
