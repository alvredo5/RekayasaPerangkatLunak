from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Produc

def index(request):
    context = {'produc_list': Produc.objects.all()}
    return render(request, "product/index.html", context)

def add(request):
    return render(request, "product/form.html")

def save(request):
    nama_product = request.POST['nama_product']
    kategori = request.POST['kategori']  
    publish = request.POST['publish']
    harga = request.POST['harga']
    jumlah_product = request.POST['jumlah_product']

    produc = Produc(
        nama_product=nama_product, 
        kategori=kategori, 
        publish=publish, 
        harga=harga, 
        jumlah_product=jumlah_product
    )
    produc.save()
    return HttpResponseRedirect(reverse('product.index'))

def edit(request, produc_id):
    produc = get_object_or_404(Produc, pk=produc_id)
    publish = produc.publish.date()
    context = {
        'id' : produc_id, 
        'nama_product' : produc.nama_product, 
        'kategori' : produc.kategori,
        'publish' : publish.strftime("%Y-%m-%d"), 
        'harga' : produc.harga, 
        'jumlah_product' :produc.jumlah_product
    }
    return render(request, 'product/form_edit.html', context)

def update(request, produc_id):
    produc = get_object_or_404(Produc, pk=produc_id)
    produc.nama_product = request.POST['nama_product']
    produc.kategori = request.POST['kategori']
    produc.publish = request.POST['publish']
    produc.harga = request.POST['harga']
    produc.jumlah_product = request.POST['jumlah_product']
    produc.save()
    return HttpResponseRedirect(reverse('product.index'))

def delete(request, produc_id):
    produc = get_object_or_404(Produc, pk=produc_id)
    produc.delete()
    return HttpResponseRedirect(reverse('product.index'))
