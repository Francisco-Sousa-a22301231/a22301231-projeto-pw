from django.shortcuts import render, redirect, get_object_or_404
from artigos.models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from artigos.forms import ComentarioForm, ArtigoForm
from django.http import JsonResponse
import logging

def artigos_view(request):
    context = context_fun()
    context['artigos'] = Artigo.objects.all()
    return render(request, 'artigos/artigos.html', context)

def artigo_view(request, id_artigo):
    context = context_fun()
    try:
        artigo = Artigo.objects.get(id=id_artigo)
        comentarios = Comentario.objects.filter(artigo=artigo)
        if request.method == 'POST':
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.artigo = artigo
                comentario.autor = request.user
                comentario.save()
        else:
            form = ComentarioForm()
        context['artigo'] = artigo
        context['comentarios'] = comentarios
        context['form'] = form
    except Artigo.DoesNotExist:
        pass
    return render(request, 'artigos/artigo.html', context)

def autor_view(request, id_artigo):
    context = context_fun()
    try:
        autor = Autor.objects.get(id=id_autor)
        context['autor'] = autor
    except:
        pass
    return render(request, 'artigos/autor.html', context)

def tema_view(request, id_tema):
    context = context_fun()
    try:
        tema = Tema.objects.get(id=id_tema)
        context['tema'] = tema
    except:
        pass
    return render(request, 'artigos/tema.html', context)

def context_fun():
    temas = Tema.objects.all()
    return {'temas' : temas}

def register_artigos(request):
    if request.user.is_authenticated:
        return redirect(reverse('artigos:home'))
    else:
        form = UserRegisterForm()
        context = {}

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                group = Group.objects.get(name='Editores de artigos')
                request.user.groups.add(group)
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for ' + username)
                return redirect(reverse('artigos:login'))
            else:
                context['message'] = "Check if you password has one uppercase letter and a number\nCheck if both passwords match\nUsernames may contain alphanumeric, _, @, +, . and - characters."

        context['form'] = form
        return render(request, 'artigos/register.html',context)

@require_POST
@login_required(login_url='login')
def update_profile_artigos(request):

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    user = request.user
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()

    return redirect(reverse('artigos:profile'))

@login_required(login_url='login')
def profile_artigos(request):
    if not request.user.is_authenticated:
        return redirect(reverse('artigos:login'))

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

    return render(request, 'artigos/profile.html', context)

def loginPage_artigos(request):
    if request.user.is_authenticated:
        return redirect(reverse('artigos:home'))
    else:
        if request.method== 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('artigos:home'))
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'artigos/login.html', context)

logger = logging.getLogger(__name__)

@require_POST
@login_required
def toggle_like(request):
    try:
        artigo_id = request.POST.get('artigo_id')
        if not artigo_id:
            raise ValueError("No artigo_id provided")
        artigo = Artigo.objects.get(id=artigo_id)
        user = request.user

        liked = False
        if user in artigo.gostos.all():
            artigo.gostos.remove(user)
        else:
            artigo.gostos.add(user)
            liked = True

        return JsonResponse({'liked': liked, 'likes_count': artigo.gostos.count()})
    except Artigo.DoesNotExist:
        logger.error(f"Artigo with id {artigo_id} does not exist")
        return JsonResponse({'error': 'Artigo not found'}, status=404)
    except Exception as e:
        logger.error(f"Error toggling like: {e}")
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def artigo_create(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save()
            return artigo_view(request, artigo.pk)
    else:
        form = ArtigoForm()
    return render(request, 'artigos/artigo_form.html', {'form': form})

@login_required
def artigo_edit(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            artigo = form.save()
            return artigo_view(request, artigo.pk)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/artigo_form.html', {'form': form})
