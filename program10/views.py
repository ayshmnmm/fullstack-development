import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

# Create your views here.
def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'Published Date', 'ISBN'])
    books = Book.objects.all().values_list('title', 'author', 'published_date', 'isbn')
    for book in books:
        writer.writerow(book)
    return response

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="books.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Book List")
    books = Book.objects.all()
    y = 700
    for book in books:
        p.drawString(100, y, f"Title: {book.title}, Author: {book.author}, Published Date: {book.published_date}, ISBN: {book.isbn}")
        y -= 30
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
