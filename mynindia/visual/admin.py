from django.contrib import admin
from .models import List_Pembelian, Product
# Register your models here.

class List_PembelianAdmin(admin.ModelAdmin):
    list_display = ("jumlah", "alamat_tujuan", "No_HP",)

admin.site.register(List_Pembelian, List_PembelianAdmin)
admin.site.register(Product)