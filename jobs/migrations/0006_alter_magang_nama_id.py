# Generated by Django 4.2.4 on 2023-08-03 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0005_alter_user_nama_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="magang",
            name="Nama_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jobs.magang"
            ),
        ),
    ]
