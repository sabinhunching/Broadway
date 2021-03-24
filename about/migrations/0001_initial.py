# Generated by Django 3.1.7 on 2021-03-24 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='about')),
            ],
        ),
    ]
