# Generated by Django 3.1.3 on 2020-11-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('client_pic', models.ImageField(blank=True, null=True, upload_to='media/portfolio')),
                ('post', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
