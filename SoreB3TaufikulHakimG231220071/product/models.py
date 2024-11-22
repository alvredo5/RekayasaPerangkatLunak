from django.db import models


class Produc(models.Model):
    nama_product = models.CharField(max_length=200)
    kategori = models.CharField(max_length=200)
    harga = models.DecimalField(max_digits=10, decimal_places=2)  
    jumlah_product = models.PositiveIntegerField()
    publish = models.DateTimeField("tanggal publikasi")

    def __str__(self):
        return self.nama_product
