# Generated by Django 2.2.7 on 2021-04-07 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210407_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books'),
        ),
    ]
