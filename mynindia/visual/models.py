from django.db import models

# Create your models here.

class Product(models.Model):
    nama_Product = models.CharField(max_length=100)
    jenis_Product = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nama_Product} {self.jenis_Product}"

class List_Pembelian(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    jumlah = models.CharField(max_length=100)
    No_HP = models.CharField(max_length=100)
    alamat_tujuan = models.TextField()

    def __str__(self):
        return f"{self.jumlah} {self.alamat_tujuan} {self.No_HP}"