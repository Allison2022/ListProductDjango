# Generated by Django 3.2.17 on 2023-03-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_alter_contact_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sex',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], default='M', max_length=1),
        ),
    ]
