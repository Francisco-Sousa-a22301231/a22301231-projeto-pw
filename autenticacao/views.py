from django.shortcuts import render, redirect
from curso.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def register(request):
    app = request.session.get('app')
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    else:
        form = UserRegisterForm()
        context = {}

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                #group = Group.objects.get(name='Editores de curso')
                #request.user.groups.add(group)
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + username)
                return redirect('autenticacao:login')
            else:
                context['message'] = "Check if you password has one uppercase letter and a number\nCheck if both passwords match\nUsernames may contain alphanumeric, _, @, +, . and - characters."

        context['form'] = form
        return render(request, 'autenticacao/register.html',context)

@require_POST
@login_required(login_url='login')
def update_profile(request):

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    user = request.user
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()

    referer = request.session.get('referrer', '/')
    return redirect(referer)  # Redirect to the previous page after update


@login_required(login_url='login')
def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('autenticacao:login'))


    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email

    context = {
        'username' : username,
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
    }

    return render(request, 'autenticacao/profile.html', context)

def loginPage(request):
    next_url = request.GET.get('next', '')

    if request.user.is_authenticated:
        return render(request, 'autenticacao/user.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return render(request, 'autenticacao/user.html')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {'next': next_url}
    return render(request, 'autenticacao/login.html', context)

def login_view(request):
    if request.method == "POST":

        # Verifica as credenciais
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            # Se as credenciais são válidas, faz login e redireciona
            login(request, user)
            return render(request, 'autenticacao/user.html')
        else:
            # Se inválidas, reenvia para login com mensagem
            render(request, 'autenticacao/login.html', {
                'mensagem':'Credenciais inválidas'
            })

            return render(request, 'autenticacao/login.html')

    # adicionar
    if request.user.is_authenticated:
        return render(request, 'autenticacao/user.html')
    else:
        return render(request, 'autenticacao/login.html')