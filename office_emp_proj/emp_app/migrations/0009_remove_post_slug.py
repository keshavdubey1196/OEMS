# Generated by Django 4.1.7 on 2023-03-06 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("emp_app", "0008_post_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
    ]
