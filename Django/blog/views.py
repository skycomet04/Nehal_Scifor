from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseForbidden
from blog.models import Contact,Blog,Comment
from django.contrib import messages
from blog.forms import BlogForm,ContactForm,CommentForm
from django.utils import timezone
from datetime import date
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from random import choice
def home(request):
    items=Blog.objects.all().order_by("-updated")[:4:1]
    itemslist=Blog.objects.all()
    items_id=[item.id for item in itemslist]
    post1_id=choice(items_id)
    items_id.remove(post1_id)
    post2_id=choice(items_id)
    post1=Blog.objects.get(id=post1_id)
    post2=Blog.objects.get(id=post2_id)
    context={
        "query":items,
        "title":"List",
        'id1':post1,
        'id2':post2,
    }
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def signin(request):
    return render(request,'signin.html')
def account(request):
    return render(request,'account.html')
def blogs(request):
    return render(request,'blogs.html')
def blogs_detail(request,id):
    instance=get_object_or_404(Blog,id=id)
    commentlist=instance.comments.all()
    context={
        "title":"instance.title",
        "instance": instance,
        'comments':commentlist,
    }
    return render(request,'blogdetail.html',context)
def blogs_list(request):
    queryset_list=Blog.objects.all().order_by("-updated")
    paginator = Paginator(queryset_list, 10) 
    page_request_var="page"
    page_obj = request.GET.get(page_request_var)
    try:
        queryset=paginator.page(page_obj)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)

    context={
        "querylist":queryset_list,
        "title":"List",
        "page_request_var":page_request_var
    }
    return render(request, "blogs.html",context)
def createblog(request):
    form = BlogForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            # Save the form but don't commit to the database yet
            blog = form.save(commit=False)
            blog.created_by=request.user
            blog.updated = timezone.now()
            blog.date = date.today()
            blog.save()
    context={'form': form,
            'is_update':False,}
    return render(request,'createblog.html',context)
def deleteblog(request,id):
    item = Blog.objects.get(id=id)
    if request.user != item.created_by:
        return HttpResponseForbidden("You don't have permission to update this blog post.")
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('blog_list')

def updateblog(request,id):
    upd_item=Blog.objects.get(id=id)
    form=BlogForm(instance=upd_item)       
    if request.user != upd_item.created_by:
        return HttpResponseForbidden("You don't have permission to update this blog post.")
    if request.method =='POST':
        form=BlogForm(request.POST, instance=upd_item)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.updated = timezone.now()
            ins.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=upd_item)
    context={'form':form,'is_update':True}
    return render(request,'createblog.html',context)
   
def contact(request):
    form1 = ContactForm(request.POST)
    if request.method == "POST":
        if form1.is_valid():
            # Save the form but don't commit to the database yet
            contact = form1.save(commit=False)
            contact.date=date.today()
            contact.save()
    context={'form':form1}    
    return render(request,'contact.html',context)

def createcomment(request,bid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            obj = form.save(commit=False)
            blog=Blog.objects.get(id=bid)
            obj.blog=blog
            obj.save()
    context={'form': form,}
    return render(request,'blogs.html',context)

def practice(request):
   return render(request,"practice.html")
