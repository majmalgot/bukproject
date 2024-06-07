from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(
        Q(title__icontains=query) | 
        Q(author__icontains=query) | 
        Q(description__icontains=query)
    ) if query else Book.objects.all()
    return render(request, 'book_list.html', {'books': books, 'query': query})

def buy_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'buy_books.html', {'books': books})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('index')  # Redirect to the home page or any other page
        else:
            messages.error(request, 'Error creating account.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

