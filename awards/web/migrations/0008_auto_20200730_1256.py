# Generated by Django 3.0.8 on 2020-07-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0007_rating_comment"),
    ]

    operations = [
        migrations.RemoveField(model_name="rating", name="assessment",),
        migrations.AlterField(
            model_name="rating",
            name="access",
            field=models.IntegerField(
                help_text="Resources are easily accessible and readily available to anyone.",
                null=True,
                verbose_name="Access",
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="comment",
            field=models.TextField(blank=True, verbose_name="Comment (optional)"),
        ),
        migrations.AlterField(
            model_name="rating",
            name="currency",
            field=models.IntegerField(
                help_text="Information is current and up to date. Date of materials is clearly indicated.",
                null=True,
                verbose_name="Currency",
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="inclusion",
            field=models.IntegerField(
                help_text="Promotes inclusiveness and diversity through the use of a variety of languages and cultural contexts.",
                null=True,
                verbose_name="Inclusion",
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="licensing",
            field=models.IntegerField(
                help_text="Copyright and Fair Use guidelines are followed with proper use of citations. An open license is clearly stated.",
                null=True,
                verbose_name="Licensing",
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="status",
            field=models.CharField(
                choices=[
                    ("empty", "Empty ballot"),
                    ("draft", "Draft rating"),
                    (
                        "conflict",
                        "Conflict of interest or can't understand the language",
                    ),
                    ("done", "Completed rating"),
                ],
                default="empty",
                max_length=20,
            ),
        ),
    ]