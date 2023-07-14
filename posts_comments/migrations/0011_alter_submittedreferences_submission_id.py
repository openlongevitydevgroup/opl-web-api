# Generated by Django 4.2.2 on 2023-07-13 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts_comments", "0010_remove_submittedreferences_submission_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submittedreferences",
            name="submission_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts_comments.submission",
            ),
        ),
    ]
