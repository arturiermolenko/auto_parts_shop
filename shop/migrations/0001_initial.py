# Generated by Django 4.2.11 on 2024-06-09 16:39

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to=shop.models.category_image_file_path
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("number", models.CharField(max_length=6, unique=True)),
                ("description", models.TextField()),
                ("materials", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("costs_prise", models.DecimalField(decimal_places=2, max_digits=16)),
                ("sell_price", models.DecimalField(decimal_places=2, max_digits=16)),
                ("link_where_buy", models.TextField()),
                (
                    "main_image",
                    models.ImageField(upload_to=shop.models.item_main_image_file_path),
                ),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="ItemImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to=shop.models.item_image_file_path),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="shop.item",
                    ),
                ),
            ],
        ),
    ]
