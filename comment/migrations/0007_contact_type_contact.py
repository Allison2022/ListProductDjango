# Generated by Django 3.2.17 on 2023-03-08 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_contact_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type_contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comment.typecontact'),
        ),
    ]