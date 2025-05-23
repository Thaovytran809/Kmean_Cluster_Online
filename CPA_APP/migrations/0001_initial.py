# Generated by Django 5.2 on 2025-04-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('year_birth', models.IntegerField()),
                ('education', models.CharField(max_length=50)),
                ('marital_status', models.CharField(max_length=50)),
                ('income', models.FloatField(blank=True, null=True)),
                ('kidhome', models.IntegerField()),
                ('teenhome', models.IntegerField()),
                ('dt_customer', models.DateField()),
                ('recency', models.IntegerField()),
                ('complain', models.BooleanField()),
                ('mnt_wines', models.FloatField()),
                ('mnt_fruits', models.FloatField()),
                ('mnt_meat_products', models.FloatField()),
                ('mnt_fish_products', models.FloatField()),
                ('mnt_sweet_products', models.FloatField()),
                ('mnt_gold_prods', models.FloatField()),
                ('num_deals_purchases', models.IntegerField()),
                ('accepted_cmp1', models.BooleanField()),
                ('accepted_cmp2', models.BooleanField()),
                ('accepted_cmp3', models.BooleanField()),
                ('accepted_cmp4', models.BooleanField()),
                ('accepted_cmp5', models.BooleanField()),
                ('response', models.BooleanField()),
                ('num_web_purchases', models.IntegerField()),
                ('num_catalog_purchases', models.IntegerField()),
                ('num_store_purchases', models.IntegerField()),
                ('num_web_visits_month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
