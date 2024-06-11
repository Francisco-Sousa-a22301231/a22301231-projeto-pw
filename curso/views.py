from django.shortcuts import render, redirect, get_object_or_404
from curso.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from forms import UserRegisterForm
from .forms import CursoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def curso_view(request):

    c = Curso.objects.all()
    for c1 in c:
        curso = c1

    disciplinas = Disciplina.objects.filter(cursos=curso)
    context = {
        'curso' : curso,
        'disciplinas' : disciplinas
    }
    return render(request, 'curso/curso.html', context)

def disciplina_view(request, id_disciplina):
    return render(request, 'curso/disciplina.html', {'disciplina' : Disciplina.objects.get(id=id_disciplina)})

def projeto_view(request, id_projeto):
    return render(request, 'curso/projeto.html', {'projeto' : Projeto.objects.get(id=id_projeto)})

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('curso:home'))
    else:
        form = UserRegisterForm()
        context = {}

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                group = Group.objects.get(name='Editores de curso')
                request.user.groups.add(group)
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + username)
                return redirect(reverse('curso:login'))
            else:
                context['message'] = "Check if you password has one uppercase letter and a number\nCheck if both passwords match\nUsernames may contain alphanumeric, _, @, +, . and - characters."

        context['form'] = form
        return render(request, 'curso/register.html',context)

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

    return redirect(reverse('curso:profile'))

@login_required(login_url='login')
def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse('curso:login'))


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

    return render(request, 'curso/profile.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect(reverse('curso:home'))
    else:
        if request.method== 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('curso:home'))
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'curso/login.html', context)


@login_required
def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            curso = form.save()
            return curso_view(request, pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/curso_form.html', {'form': form})

