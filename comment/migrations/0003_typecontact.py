# Generated by Django 3.2.17 on 2023-02-26 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typecontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
