from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

from apps.public.forms import NewUserForm, ProfileRegisterForm


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# def register(request):
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('/')
#     return render(request, 'register.html', {'form': form})
def register(request):
    # if request.method == 'POST':
    form = NewUserForm(request.POST)

    if form.is_valid():
        user = form.save()
        user.refresh_from_db()  # load the profile instance created by the signal
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        messages.success(request, f'Your account has been sent for approval!')
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'index.html')

    else:
        form = NewUserForm()

        context = {
            'form': form,

        }
        return render(request, 'register.html', context)


def appointments(request):
    return render(request, "appointments.html")

def s(request):
    return render(request, "s.html")

# faltan agregar los camposy realizar tests
