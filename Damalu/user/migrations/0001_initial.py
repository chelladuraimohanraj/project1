# Generated by Django 3.0.7 on 2020-08-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('rate', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='uploads')),
            ],
        ),
    ]
