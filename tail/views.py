from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import objectDetailMixin
from .forms import TagForm


# Create your views here..
def posts_list(request):
	posts = Post.objects.all()
	return render(request, 'tail/index.html', context={'posts': posts})


class PostDetail(objectDetailMixin, View):
	model = Post
	template = 'tail/post_detail.html'


class TagDetail(objectDetailMixin, View):
	model = Tag
	template = 'tail/tag_detail.html'

class TagCreate(View):
	def get(self, request):
		form = TagForm()
		return render(request, 'tail/tag_create.html', context={'form':form})

	def post(self, request):
		bound_form = TagForm(request.POST)

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect(new_tag)
		return render(request, 'tail/tag_create.html', context={'form': bound_form})



def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'tail/tags_list.html', context={'tags': tags})

