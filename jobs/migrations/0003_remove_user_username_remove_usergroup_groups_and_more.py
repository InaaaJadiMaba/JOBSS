# Generated by Django 4.2.4 on 2023-08-03 03:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0002_usergroup_alter_magang_file_staff_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.RemoveField(
            model_name="usergroup",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="usergroup",
            name="user_permissions",
        ),
        migrations.DeleteModel(
            name="Staff",
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.DeleteModel(
            name="usergroup",
        ),
    ]
