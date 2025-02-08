from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

# @login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, "books/book_list.html", {"books": books})

# @login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("book-list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})

# @login_required
def book_detail(request,pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if book:
        print(book)
    return render(request, "books/book_detail.html", {"book": book})

# @login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book-list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})

# @login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    book.delete()
    return redirect("book-list")
    # return render(request, "books/book_confirm_delete.html", {"book": book})
