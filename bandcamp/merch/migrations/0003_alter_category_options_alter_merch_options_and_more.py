# Generated by Django 4.2.2 on 2023-06-19 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
        ('merch', '0002_remove_category_sub_category_subcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='merch',
            options={'verbose_name': 'merch', 'verbose_name_plural': 'merches'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'sub category', 'verbose_name_plural': 'sub categories'},
        ),
        migrations.AlterField(
            model_name='merch',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merches', to='music.album', verbose_name='album'),
        ),
        migrations.AlterField(
            model_name='merch',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merches', to='merch.subcategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='merch',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='merch.category', verbose_name='category'),
        ),
    ]
