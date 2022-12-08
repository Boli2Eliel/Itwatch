from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

#Resgistration
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

#=======REGISTER FUNCTION=========
@login_required()
def register(request):
    """if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = form.cleaned_data.get('username')
            messages.success(request, f"{new_user} enregistré avec succès!")
            return redirect('dashboard-index')
    else:
        form = CreateUserForm()

    title = "Enregistrer un utilisateur"
    context = {
        'title': title,
        'form': form,
    }
    return render(request, "user/register.html", context)"""
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Huff ,Username already exist')
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Come On, Email was already Taken !')
            return redirect("register")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            mydict = {'username': username}
            user.save()
            html_template = 'register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to Service-Verse'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect("success")
    else:
        return render(request, 'user/register.html')


#=======END REGISTER FUNCTION=========

#================
def logon(request):
    title = "Connectez-vous à IT'WATCH suite"
    context = {
        "title": title,
    }
    return render(request, "partials/logon.html", context)
#================


#========PROFIL & PROFILE UPDATE=========

@login_required()  # on met ce "decorators" partout où l'on veut que le user soit connecté avant d'y acceder
def profile(request):
    return render(request, 'user/profile.html')

@login_required() #"LOGIN_URL = 'user-login'" # for decorators a été ajouté dans le settings
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/profile_update.html', context)

# ========END PROFILE & PROFILE UPDATE========



"""def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, " Bienvenue à AMC Assurance - IT'WATCH")
            return redirect('dashboard-index')

        else:
            messages.error(request, "Erreur d'authentification: Verifier votre iD ou mot de passe")

    return render(request, 'user/login.html', {})


def first_page(request):
    title = "Bienvenue sur IT'WATCH"
    context = {
        "title": title,
    }
    return render(request, "partials/first_page.html", context)"""