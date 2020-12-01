from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse
from .models import *

def main(request):

	try:
		return render(request, 'web/main.html')

	except Exception:
		return HttpResponse(status=404)

def menu(request, page):

	try:
		if page == "company" or page == "history" or page == "organization" or page == "map" or page == "management":
			return render(request, 'web/menu_1.html', {'page':page})

		elif page == "business" or page == "major":
			return render(request, 'web/menu_2.html', {'page':page})

		elif page == "result":
			result_posts_all = Result_post.objects.all().order_by('-id')
			page_number = int(request.GET.get('p', 1))
			pagenator = Paginator(result_posts_all, 11)
			result_posts = pagenator.get_page(page_number)
			return render(request, 'web/menu_3.html', {'page':page, 'result_posts':result_posts})

		elif page == "equipment":
			return render(request, 'web/menu_4.html', {'page':page})

		elif page == "license":
			return render(request, 'web/menu_5.html', {'page':page})

		elif page == "notice" or page == "information":
			if page == 'notice':
				notice_posts_all = Notice_post.objects.all().order_by('-id')
				page_number = int(request.GET.get('p', 1))
				pagenator = Paginator(notice_posts_all, 11)
				notice_posts = pagenator.get_page(page_number)
				return render(request, 'web/menu_6.html', {'page':page, 'notice_posts':notice_posts})

			elif page == 'information':
				information_posts_all = Information_post.objects.all().order_by('-id')
				page_number = int(request.GET.get('p', 1))
				pagenator = Paginator(information_posts_all, 11)
				information_posts = pagenator.get_page(page_number)
				return render(request, 'web/menu_6.html', {'page':page, 'information_posts':information_posts})

	except Exception:
		return HttpResponse(status=404)

def detail_post(request, page, post_pk):

	try:
		if page == 'notice':
			notice_post = get_object_or_404(Notice_post, pk=post_pk)
			return render(request, 'web/detail_notice.html', {'notice_post':notice_post})

		elif page == 'information':
			success = 0
			name = 'enter'
			information_post = get_object_or_404(Information_post, pk=post_pk)
			if request.method == "POST":
				if request.POST['post_password'] == information_post.password:
					return render(request, 'web/detail_information.html', {'page':page,'information_post':information_post})
				else:
					return render(request, 'web/check_password_information_post.html', {'page':page, 'success':success, 'name':'enter'})

		elif page == 'result':
			result_post = get_object_or_404(Result_post, pk=post_pk)
			return render(request, 'web/detail_result.html', {'page':page, 'result_post':result_post})

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

	try:
		if request.method == "POST":
			Information_post.objects.create(
				author=request.POST['author'],
				password=request.POST['password'],
				phone_number=request.POST['phone_number'],
				title=request.POST['title'],
				text=request.POST['text'],
				file_1=request.POST['file_1'],
				file_2=request.POST['file_2'],
				file_3=request.POST['file_3'],
				file_4=request.POST['file_4'],
				file_5=request.POST['file_5'],
			)
			information_posts_all = Information_post.objects.all().order_by('-id')
			page_number = int(request.GET.get('p', 1))
			pagenator = Paginator(information_posts_all, 11)
			information_posts = pagenator.get_page(page_number)
			return render(request, 'web/menu_6.html', {'page':page, 'information_posts':information_posts})

		else:
			return render(request, 'web/new_information_post.html', {'page':page})

	except Exception:
		return HttpResponse(status=404)
