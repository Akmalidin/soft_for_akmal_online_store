# Generated by Django 4.1.12 on 2024-09-07 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_options_rename_name_category_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeofprice',
            options={'verbose_name': 'Тип цены', 'verbose_name_plural': 'Типы цен'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
