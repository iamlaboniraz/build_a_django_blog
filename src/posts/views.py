from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm
from .models import Posts

# Create your views here.
def post_create(request):
	form=PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		print (form.cleaned_data.get("title"))
		instance.save()
		return redirect("../")
	context={
	   "form":form
	}   
	return render(request,"post_form.html",context)

def post_detail(request,id=None):
	instance=get_object_or_404(Posts,id=id)
	context={
	  "title":instance.title,
	  "instance":instance,
	}
	return render(request,"post_detail.html",context)

def post_list(request):
	queryset_list = Posts.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 9) # Show 25 contacts per page

	page_request_var = "pageList"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context={
	   "object_list":queryset,
	   "title":"List",
	   "page_request_var": page_request_var
	}
	return render(request,"post_list.html",context)



def post_update(request,id=None):
	instance=get_object_or_404(Posts,id=id)
	form=PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"<a href=''>Post</a>update Successfully!!",extra_tags="html_safe")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
	   "title":instance.title,
	   "form":form,
	   "instance":instance
	}	
	return render(request,"post_form.html",context)
def post_delete(request,id=None):
	instance=get_object_or_404(Posts,id=id)
	instance.delete()
	messages.success(request,"Successfully deleted!!")
	return redirect("posts:list")
