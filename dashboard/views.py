from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#import paginator stuff
from django.core.paginator import Paginator
from .forms import ProductForm
from django.contrib.auth.models import User

# Create your views here.
@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def index(request):
    title = "Bienvenue sur IT'WATCH"
    context = {
        'title': title
    }
    return render(request, 'dashboard/index.html', context)

@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def staff(request):
    workers = User.objects.all()

    title = "Staff Page"
    context = {
        'title': title,
        'workers': workers,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required()
def staff_detail(request, id):
    workers = User.objects.get(pk=id)

    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required()
def add_product(request):
    return render(request, "add_product.html")

@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def product(request):
    #p = Paginator(Product.objects.raw('SELECT * FROM dashboard_product'), 6)#Using ORM
    p = Paginator(Product.objects.all(), 6) #Pagination par 9, c-à-d chaque page affichera 9 élements #Usisng SQL
    page = request.GET.get('page')
    queryset = p.get_page(page)
    nums = "a" * queryset.paginator.num_pages #POUR AFFICHER LE NOMBRE EXACT DES PAGES et afiicher le nombres exact

    #----Ajout matériel----
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Matériel ajouté avec succès")
            return redirect('dashboard-product')  # puis on redirige vers la page de la liste
    else:
        form = ProductForm()
    # ----End Ajout matériel----

    # ----- Mise à jour matériel ----

    # ------ end mise à jour -------

    title = "Liste du matériel"
    context = {
        'title': title,
        'queryset': queryset,
        'nums': nums,
        'form' : form,
    }
    return render(request, 'dashboard/product.html', context)

@login_required()
def update_items(request, id):
    item = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():  # verification si les infos sont valides
            form.save()  # si valide on sauvergarde le formulaire
            messages.success(request, "Mise à jour du matériel effectué avec succès")
            return redirect('dashboard-product')  # puis on redirige vers la page de la liste
    else:
        form = ProductForm(instance=item)

    context = {
        'item': item,
        'form':form,
    }
    return render(request, "dashboard/update_items.html", context)

@login_required()
def delete_item(request, id):
    pi = Product.objects.get(pk=id)
    pi.delete()
    messages.success(request, "Matériel supprimé avec succès")
    return redirect('dashboard-product')
    # messages.success(request, "Item supprimé avec succès")


@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def order(request):
    orders = Order.objects.all()

    title = "Commandes"
    context = {
        'title': title,
        'orders':orders,
    }
    return render(request, 'dashboard/order.html', context)