from recs.models import Book_list

def run():
	q = Book_list.objects.all()
	q.delete()