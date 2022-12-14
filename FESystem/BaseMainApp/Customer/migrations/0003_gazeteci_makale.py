# Generated by Django 4.1 on 2022-08-30 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_customer_detail_alter_customer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gazeteci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=120)),
                ('soyisim', models.CharField(max_length=120)),
                ('biyografi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=120)),
                ('aciklama', models.CharField(max_length=200)),
                ('metin', models.TextField()),
                ('sehir', models.CharField(max_length=120)),
                ('yayımlanma_tarihi', models.DateField()),
                ('aktif', models.BooleanField(default=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('güncelleneme_tarihi', models.DateTimeField(auto_now=True)),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to='Customer.gazeteci')),
            ],
        ),
    ]
