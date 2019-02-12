from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q

def posts_list(request):
	search_querty = request.GET.get('search', '')
	
	if search_querty:
		posts = Post.objects.filter(Q(title__icontains=search_querty) | Q(body__icontains=search_querty))
	else:
		posts = Post.objects.all()

	paginator = Paginator(posts, 10)
	
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context = {
		'page_object': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
	}


	# http://127.0.0.1:8000/tail/?page=1&

	return render(request, 'tail/index.html', context=context)


class PostDetail(objectDetailMixin, View):
	model = Post
	template = 'tail/post_detail.html'

class PostCreate(LoginRequiredMixin, objectCreateMixin, View):
	model_form = PostForm
	template = 'tail/post_create_form.html'
	raise_exception = True

class PostUpdate(LoginRequiredMixin, objectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'tail/post_update_form.html'
	raise_exception = True

class PostDelete(LoginRequiredMixin, objectDeleteMixin, View):
	model = Post
	template = 'tail/post_delete_form.html'
	redirect_url = 'posts_list_url'
	raise_exception = True


class TagDetail(objectDetailMixin, View):
	model = Tag
	template = 'tail/tag_detail.html'

class TagCreate(LoginRequiredMixin, objectCreateMixin, View):
	model_form = TagForm
	template = 'tail/tag_create.html'
	raise_exception = True

class TagUpdate(LoginRequiredMixin, objectUpdateMixin, View):
	model = Tag
	model_form = TagForm
	template = 'tail/tag_update_form.html'
	raise_exception = True

class TagDelete(LoginRequiredMixin, objectDeleteMixin, View):
	model = Tag
	template = 'tail/tag_delete_form.html'
	redirect_url = 'tags_list_url'
	raise_exception = True



def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'tail/tags_list.html', context={'tags': tags})



