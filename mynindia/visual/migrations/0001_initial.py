# Generated by Django 4.2.7 on 2023-11-12 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_Product', models.CharField(max_length=100)),
                ('jenis_Product', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='List_Pembelian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.CharField(max_length=100)),
                ('No_HP', models.CharField(max_length=100)),
                ('alamat_tujuan', models.TextField()),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visual.product')),
            ],
        ),
    ]
