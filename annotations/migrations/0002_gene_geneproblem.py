# Generated by Django 4.2.2 on 2023-07-16 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("open_problems", "0006_rename_question_id_openproblems_problem_id_and_more"),
        ("annotations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gene",
            fields=[
                ("gene_id", models.AutoField(primary_key=True, serialize=False)),
                ("gene_name", models.CharField(max_length=50, unique=True)),
                ("gene_symbol", models.CharField(max_length=10, unique=True)),
                (
                    "species",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="annotations.species",
                    ),
                ),
            ],
            options={
                "db_table": "Genes",
                "db_table_comment": "Table for all genes",
            },
        ),
        migrations.CreateModel(
            name="GeneProblem",
            fields=[
                ("annotation_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "gene_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="annotations.gene",
                    ),
                ),
                (
                    "open_problem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="open_problems.openproblems",
                    ),
                ),
            ],
            options={
                "db_table_comment": "Relation table for each gene and open problem",
            },
        ),
    ]