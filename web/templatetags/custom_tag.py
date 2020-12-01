from django import template

register = template.Library()

@register.filter
def title_slice(title):
	if len(title) > 40:
		title = title[:40] + '...'
		return title
	else :
		return title

@register.filter
def file_name_slice(file_name):
	file_name = file_name.replace('/media/files/',"")
	return file_name
