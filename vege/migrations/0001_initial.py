# Generated by Django 4.2.3 on 2023-07-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recepies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipie_name', models.CharField(max_length=100)),
                ('recipie_description', models.TextField()),
                ('recipie_image', models.ImageField(upload_to='recepie')),
            ],
        ),
    ]
