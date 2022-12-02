from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#import paginator stuff
from django.core.paginator import Paginator
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User

# Create your views here.
#===================INDEX========================
@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def index(request):
    orders = Order.objects.all()
    orders1 = Order.objects.values('product')
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            messages.success(request, "Requête enregistrée avec succès !")
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
    # *****************For Product*********************
    ltp = Product.objects.filter(categorie='Laptop').count()
    laptop = int(ltp)

    dtp = Product.objects.filter(categorie='Desktop').count()
    desktop = int(dtp)

    onl = Product.objects.filter(categorie='Onduleur').count()
    onduleur = int(onl)

    imp = Product.objects.filter(categorie='Imprimante').count()
    imprimante = int(imp)

    svr = Product.objects.filter(categorie='Serveur').count()
    serveur = int(svr)

    ecr = Product.objects.filter(categorie='Ecran').count()
    ecran = int(ecr)

    nas = Product.objects.filter(categorie='Nas').count()
    nas = int(nas)

    fon= Product.objects.filter(categorie='Phone').count()
    phone = int(fon)

    pabx = Product.objects.filter(categorie='IPABX').count()
    ipabx = int(pabx)

    otr = Product.objects.filter(categorie='Autre').count()
    autre= int(otr)
            #**********
    categorie_list = [
    'Laptop', 'Desktop', 'Onduleur','Imprimante', 'Serveur','Ecran',
    'Nas', 'Phone', 'IPABX', 'Autre'
    ]
    number_list = [
        laptop, desktop, onduleur, imprimante, serveur, ecran, nas,
        phone, ipabx, autre
    ]
    #*****************For order **********************
    lp = Order.objects.filter(category='Laptop').count()
    lap = int(lp)

    dp = Order.objects.filter(category='Desktop').count()
    desk = int(dp)

    ond = Order.objects.filter(category='Onduleur').count()
    ond = int(ond)

    prt = Order.objects.filter(category='Imprimante').count()
    prt = int(prt)

    sv = Order.objects.filter(category='Serveur').count()
    sv= int(sv)

    ec = Order.objects.filter(category='Ecran').count()
    ec = int(ec)

    nasd = Order.objects.filter(category='Nas').count()
    nasd = int(nasd)

    fone= Order.objects.filter(category='Téléphonie').count()
    fone = int(fone)

    accs = Order.objects.filter(category='Accessoires').count()
    accs = int(accs)

    otre = Order.objects.filter(category='Autre').count()
    otre= int(otre)
            #**********
    order_categorie = [
    'Laptop', 'Desktop', 'Onduleur','Imprimante', 'Serveur','Ecran',
    'Nas', 'Phone', 'Accesoires', 'Autre'
    ]
    order_number = [
        lap, desk, ond, prt, sv, ec, nasd,
        fone, accs, otre
    ]
    

    #******************************************
    title = "Bienvenue sur IT'WATCH"
    context = {
        'title': title,
        'orders': orders,
        'orders1': orders1,
        'form': form,
        'products': products,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
        'categorie_list': categorie_list,
        'number_list': number_list,
        'order_categorie': order_categorie,
        'order_number': order_number,
    }
    return render(request, 'dashboard/index.html', context)

#=======================STAFF==========================
@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()

    title = "Staff Page"
    context = {
        'title': title,
        'workers': workers,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/staff.html', context)

#======================== STAFF DETAIL =========================
@login_required()
def staff_detail(request, id):
    workers = User.objects.get(pk=id)

    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff_detail.html', context)

#======================= ADD PRODUCT =======================
@login_required()
def add_product(request):
    return render(request, "add_product.html")

#======================= PRODUCT =========================
@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def product(request):
    #p = Paginator(Product.objects.raw('SELECT * FROM dashboard_product'), 6)#Using ORM
    p = Paginator(Product.objects.all(), 6) #Pagination par 9, c-à-d chaque page affichera 9 élements #Usisng SQL
    page = request.GET.get('page')
    queryset = p.get_page(page)
    nums = "a" * queryset.paginator.num_pages #POUR AFFICHER LE NOMBRE EXACT DES PAGES et afiicher le nombres exact

#*********************************************
    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()
#*********************************************

    #product_graphs = Product.objects.filter('categorie')

    #----Ajout matériel----
    if request.method == 'POST':
        form = ProductForm(request.POST or '')
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('identifiant')
            product_modele = form.cleaned_data.get('marque_modele')
            messages.success(request, f"{product_name}-{product_modele} a été ajouté avec succès")
            return redirect('dashboard-product')  # puis on redirige vers la page de la liste
    else:
        form = ProductForm()
    # ----End Ajout matériel----

    # ----- Count items -------


    title = "Liste du matériel"
    context = {
        'title': title,
        'queryset': queryset,
        'nums': nums,
        'form' : form,
        'workers_count': workers_count,
        'products_count': products_count,
        'orders_count': orders_count,
        #'product_graphs': product_graphs,
    }
    return render(request, 'dashboard/product.html', context)

#===================== UPDATE ITEMS ========================
@login_required()
def update_items(request, id):
    item = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():  # verification si les infos sont valides
            form.save()  # si valide on sauvergarde le formulaire
            update_name = form.cleaned_data.get('identifiant')
            update_modele = form.cleaned_data.get('marque_modele')
            messages.success(request, f"Mise à jour de {update_name}-{update_modele} effectué avec succès")
            return redirect('dashboard-product')  # puis on redirige vers la page de la liste
    else:
        form = ProductForm(instance=item)

    context = {
        'item': item,
        'form':form,
    }
    return render(request, "dashboard/update_items.html", context)

#====================== DELETE ITEMS ========================
@login_required()
def delete_item(request, id):
    pi = Product.objects.get(pk=id)
    pi.delete()
    messages.success(request, "Matériel supprimé avec succès")
    return redirect('dashboard-product')
    # messages.success(request, "Item supprimé avec succès")

#======================== ORDER ========================
@login_required()  # on met ce "decorators" pârtout où l'on veut que le user soit connecté avant d'y acceder
def order(request):
    orders = Order.objects.all()

    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    orders_count = Order.objects.all().count()

    title = "Commandes"
    context = {
        'title': title,
        'orders':orders,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
    }
    return render(request, 'dashboard/order.html', context)