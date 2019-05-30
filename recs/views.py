from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Book_list, Recommended_list

# Create your views here.
def index(request):
	all_books = Book_list.objects.all()
	context = {'all_books':all_books}
	return render(request, 'recs/index.html',context)

def details(request, book_id):
	book = Recommended_list.objects.get(idx=book_id)
	all_books = Book_list.objects.all()
	li = []
	li.append(all_books[book.rec1-1].name)
	li.append(all_books[book.rec2-1].name)
	li.append(all_books[book.rec3-1].name)
	li.append(all_books[book.rec4-1].name)
	li.append(all_books[book.rec5-1].name)
	
	context = {'book':book, 'li':li}
	return render(request, 'recs/details.html', context)