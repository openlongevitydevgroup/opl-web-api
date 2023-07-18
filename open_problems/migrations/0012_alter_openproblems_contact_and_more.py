# Generated by Django 4.2.2 on 2023-07-17 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("open_problems", "0011_remove_openproblems_reference_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="openproblems",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="open_problems.contact",
            ),
        ),
        migrations.AlterField(
            model_name="submittedproblems",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="open_problems.contact",
            ),
        ),
    ]