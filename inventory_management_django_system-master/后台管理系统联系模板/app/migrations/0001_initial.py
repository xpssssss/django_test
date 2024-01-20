# Generated by Django 4.1 on 2022-12-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("cartId", models.CharField(max_length=20)),
                ("userId", models.CharField(max_length=20)),
                ("userName", models.CharField(max_length=15)),
                ("wareId", models.CharField(max_length=20)),
                ("wareName", models.CharField(max_length=15)),
                (
                    "wareCount",
                    models.DecimalField(decimal_places=0, default=0, max_digits=10),
                ),
                ("createTime", models.DateTimeField(auto_now_add=True)),
                ("updateTime", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("orderId", models.CharField(max_length=20)),
                ("userId", models.CharField(max_length=20)),
                ("userName", models.CharField(max_length=15)),
                ("wareId", models.CharField(max_length=20)),
                ("wareName", models.CharField(max_length=15)),
                (
                    "wareCount",
                    models.DecimalField(decimal_places=0, default=0, max_digits=10),
                ),
                ("createTime", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sales",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("salesId", models.CharField(max_length=20)),
                ("yearName", models.CharField(max_length=5)),
                (
                    "yearSales",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("yearEvents", models.CharField(default="", max_length=30)),
                ("monthSales", models.JSONField(null=True)),
                ("wareSales", models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("userId", models.CharField(max_length=20)),
                ("userName", models.CharField(max_length=15, unique=True)),
                ("userPassword", models.CharField(max_length=20)),
                (
                    "userPower",
                    models.DecimalField(decimal_places=0, default=10, max_digits=3),
                ),
                ("createTime", models.DateTimeField(auto_now_add=True)),
                ("updateTime", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ware",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("wareId", models.CharField(max_length=20)),
                ("wareName", models.CharField(max_length=15, unique=True)),
                (
                    "warePower",
                    models.DecimalField(decimal_places=0, default=0, max_digits=8),
                ),
                (
                    "wareCount",
                    models.DecimalField(decimal_places=0, default=0, max_digits=10),
                ),
                ("createTime", models.DateTimeField(auto_now_add=True)),
                ("updateTime", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
