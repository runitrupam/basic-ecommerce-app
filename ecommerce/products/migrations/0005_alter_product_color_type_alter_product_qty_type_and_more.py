# Generated by Django 4.1 on 2022-09-03 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_color_type_alter_product_qty_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.quantityvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.sizevariant'),
        ),
    ]