# Generated by Django 4.2.16 on 2024-09-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdb', '0002_alter_db_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='db',
            name='email',
            field=models.EmailField(max_length=254, null='True'),
            preserve_default='True',
        ),
    ]
