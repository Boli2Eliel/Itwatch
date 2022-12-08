import datetime

#import paginator stuff
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from .forms import OrderForm, ProductForm
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Import XlS
import xlwt

import csv

#====Import PDF====
import io
# ---xhtml2pdf---
from django.http import FileResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab

#Resgistration
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings



#Generate PDF File Product list

def show_pdf(request):
    """#create Bytestream buffer
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    # Add some lines of text
    #lines =[
        #"mlkjhjhkclslkcjkllc",
        #"mlkjhjhkclslkcjkllc",
        #"mlkjhjhkclslkcjkllc",
    #]
    products = Product.objects.all()
    #Create blank list
    lines =[]

    for product in products:
        lines.append(product.identifiant)
        lines.append(product.categorie)
        lines.append(product.etat)
        lines.append(" ")
    #loop
    for line in lines:
        textob.textLine(line)
    #finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    #Return something
    return FileResponse(buf, as_attachment=True, filename="Itwatch.pdf")"""

    products = Product.objects.all()
    date_time = str(datetime.datetime.now())
    context = {
        'products': products,
        'date_time': date_time,
    }
    return render(request, 'pdfs/show_pdf.html', context)

def export_pdf(request):
    products = Product.objects.all()

    template_path = 'pdfs/show_pdf.html'
    context = {}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=ItWatch'+\
        str(datetime.datetime.now())+ '.pdf'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response,)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#Generate text file product list
def product_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=parcItwatch.txt'
    #designate the model
    products = Product.objects.all()

    lines = []
    #Loop Thu and output
    for product in products:
        lines.append(f"{product.id},{product.identifiant},{product.marque_modele},{product.categorie},{product.noSerie},{product.etat}, {product.affecte_a}, {product.departement},{product.date_affectation}, {product.observation}\n")

    #Write to Textfile
    response.writelines(lines)
    return response

#Generate csv file product list
def product_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=parcItwatch.csv'

    # Create a csv writer
    writer = csv.writer(response)

    #designate the model
    products = Product.objects.all()

    #Add columns to csv file
    writer.writerow(['Id', 'Identifiant', 'Marque & Modèle', 'Catégorie', 'NoSérie', 'Etat du matériel', 'Affecté à', 'Departement',"Date d'affectation", "Date d'achat", 'Observations',])


    #Loop Thu and output
    for product in products:
        writer.writerow([product.id, product.identifiant, product.marque_modele, product.categorie, product.noSerie, product.etat, product.affecte_a, product.departement, product.date_affectation, product.date_achat, product.observation])

    return response

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ItWatch'+\
        str(datetime.datetime.now())+ '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Itwatch')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID', 'IDENTIFIANT', 'MARQUE & MODELE', 'CATEGORIE', 'No SERIE', 'ETAT DU MATERIEL', 'AFFECTE A', 'DEPARTEMENT',"DATE D'AFFECTATION", "DATE D'ACHAT", 'OBSERVATIONS',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_style.font.italic =True

    rows = Product.objects.values_list('id', 'identifiant', 'marque_modele', 'categorie', 'noSerie', 'etat', 'affecte_a', 'departement',"date_affectation", "date_achat", 'observation',)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


"""def product_xlsx(request):
    # designate the model
    products = Product.objects.all()
    data = []
    # Loop Thu and output
    for product in products:
        data.append({
           "ID": product.id,
            "Identifiant":product.identifiant,
            "Marque & modèle":product.marque_modele,
            "Categorie":product.categorie,
            "NoSerie":product.noSerie,
            "Etat":product.etat,
            "Affecté à":product.affecte_a,
            "Departement":product.departement,
            "Date d'affectation":product.date_affectation,
            "Date d'achat":product.date_achat,
            "Observations":product.observation
        })

    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status':200
    })"""


# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Oups ,Cet utilisateur existe déjà !')
            return redirect("user-register")
        #elif User.objects.filter(email=email).exists():
            #messages.info(request, 'Come On, Email was already Taken !')
            #return redirect("user-register")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email,)
            mydict = {'username': username,
                      'password': password,
                      'email': email,
                      }
            user.save()
            html_template = 'register_email/register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = "Bienvenue à IT'Watch-Suite"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            messages.success(request, 'Utilisateur enregistré avec success !')
            return redirect("user-register")
    else:
        return render(request, 'user/register.html')

def success(request, username=None):
    user = User.objects.create_user(username=username)
    mydict = {'username': username}
    return render(request, "user/success.html", mydict)


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
    pi = Product.objects.all().order_by('-updated_at')
    p = Paginator(pi, 6) #Pagination par 9, c-à-d chaque page affichera 9 élements #Usisng SQL
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
    orders = Order.objects.all().order_by('-date')

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