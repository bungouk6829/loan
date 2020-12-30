from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone
from .models import *

def main(request):

	try:
		return render(request, 'web/main.html')

	except Exception:
		return HttpResponse(status=404)

def menu(request, page):

	try:
		if page == "company" or page == "map":
			return render(request, 'web/menu_1.html', {'page':page})

		elif page == "worker" or page == "business" or page =="woman" or page == "jobless" or page == "cosmetic" or page == "estate" or page == "gold" or page == "leisure" or page == "car" or page == "motor":
			return render(request, 'web/loan_info.html', {'page':page})

		elif page == 'information':
			information_posts_all = Information_post.objects.all().order_by('-id')
			page_number = int(request.GET.get('p', 1))
			pagenator = Paginator(information_posts_all, 11)
			information_posts = pagenator.get_page(page_number)
			return render(request, 'web/menu_4.html', {'page':page, 'information_posts':information_posts})

		elif page == 'qna':
			return render(request, 'web/menu_4.html', {'page':page})

		elif page == 'investor':
			return render(request, 'web/menu_5.html', {'page':page})

	except Exception:
		return HttpResponse(status=404)

def detail_post(request, page, post_pk):

	try:
		if page == 'information':
			success = 0
			name = 'enter'
			information_post = get_object_or_404(Information_post, pk=post_pk)
			if request.method == "POST":
				if request.POST['post_password'] == information_post.password:
					return render(request, 'web/detail_information.html', {'page':page,'information_post':information_post})
				else:
					return render(request, 'web/check_password_information_post.html', {'page':page, 'success':success, 'name':'enter'})

	except Exception:
		return HttpResponse(status=404)

def edit_information(request, page, post_pk, name):

	try:
		success = 0
		if page == 'information':
			information_post = get_object_or_404(Information_post, pk=post_pk)
			if name == 'delete':
				if request.POST['post_password'] == information_post.password:
					information_post.delete()
					success = 1
		return render(request, 'web/check_password_information_post.html', {'name':name, 'page':page, 'success':success})

	except Exception:
		return HttpResponse(status=404)

def input_information_post_password(request, page, post_pk, name):

	try:
		information_post = get_object_or_404(Information_post, pk=post_pk)
		return render(request, 'web/input_information_post_password.html', {'page':page, 'information_post':information_post, 'name':name})

	except Exception:
		return HttpResponse(status=404)

def new_information_post(request, page):

		if request.method == "POST":
			title_data = str(request.POST.get('title','대출문의합니다.'))
			text_data = str(request.POST.get('text','대출문의합니다.'))
			password_data = str(request.POST.get('password','1234'))
			Information_post.objects.create(
				name=request.POST['name'],
				age=request.POST['age'],
				money=request.POST['money'],
				product=request.POST['product'],
				job=request.POST['job'],
				region_1=request.POST['region_1'],
				region_2=request.POST['region_2'],
				password=password_data,
				phone_number=request.POST['phone_number'],
				title=title_data,
				text=text_data
			)
			information_posts_all = Information_post.objects.all().order_by('-id')
			page_number = int(request.GET.get('p', 1))
			pagenator = Paginator(information_posts_all, 11)
			information_posts = pagenator.get_page(page_number)
			return render(request, 'web/menu_4.html', {'page':page, 'information_posts':information_posts})

		else:
			return render(request, 'web/new_information_post.html', {'page':page})
