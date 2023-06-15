# Generated by Django 4.2.2 on 2023-06-15 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('cover', models.ImageField(upload_to='music/', verbose_name='cover')),
                ('release_date', models.DateField(default=None, verbose_name='release_date')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='summary')),
                ('realese_type', models.IntegerField(choices=[(0, 'None'), (1, 'Single'), (2, 'EP'), (3, 'Album')], default=0, verbose_name='realese_type')),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('audio', models.FileField(blank=True, null=True, upload_to='music/', verbose_name='audio')),
                ('duration', models.CharField(max_length=5, verbose_name='duration')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.album', verbose_name='album')),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
            },
        ),
    ]
