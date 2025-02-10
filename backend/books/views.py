from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm


def book_list(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(user=request.user)
        return render(request, "books/book_list.html", {"books": books})
    messages.error(request,"Please Login First")
    return redirect('login')




def book_create(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = BookForm(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return redirect("book-list")
        messages.error(request,"Please Login First")
        return redirect('login')
        
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})


def book_detail(request,pk):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, pk=pk, user=request.user)
        if book:
            print(book)
        return render(request, "books/book_detail.html", {"book": book})
    messages.error(request,"Please Login First")
    return redirect('login')



def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect("book-list")
        messages.error(request,"Please Login First")
        return redirect('login')
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})


def book_delete(request,pk):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect("book-list")
    messages.error(request,"Please Login First")
    return redirect('login')
    # return render(request, "books/book_confirm_delete.html", {"book": book})