# Generated by Django 4.2.2 on 2023-07-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts_comments", "0014_alter_comments_parent"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comments",
            new_name="Comment",
        ),
    ]