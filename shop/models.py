import os.path
import uuid

from django.db import models
from django.utils.text import slugify


def file_path(instance, filename, suffix, folder) -> str:
    _, ext = os.path.splitext(filename)
    filename = f"{suffix}-{uuid.uuid4()}{ext}"
    return os.path.join(f"uploads/images/{folder}", filename)


def category_image_file_path(instance, filename) -> str:
    return file_path(instance, filename, instance.name, "categories")


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(null=True, upload_to=category_image_file_path)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


def item_main_image_file_path(instance, filename) -> str:
    return file_path(instance, filename, f"main_{instance.name}", "items")


class Item(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=6, unique=True)
    description = models.TextField()
    materials = models.CharField(max_length=255)
    quantity = models.IntegerField()
    costs_prise = models.DecimalField(max_digits=16, decimal_places=2)
    sell_price = models.DecimalField(max_digits=16, decimal_places=2)
    link_where_buy = models.TextField()
    main_image = models.ImageField(upload_to=item_main_image_file_path)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category"
    )

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.number} {self.name}"


def item_image_file_path(instance, filename) -> str:
    return file_path(instance, filename, instance.item.name, "items")


class ItemImage(models.Model):
    image = models.ImageField(upload_to=item_image_file_path)
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="images"
    )
