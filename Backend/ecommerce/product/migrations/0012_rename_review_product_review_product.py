# Generated by Django 5.1.4 on 2025-01-06 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_product',
            new_name='product',
        ),
    ]