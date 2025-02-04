# Generated by Django 4.2 on 2024-08-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="product_like",
            field=models.ManyToManyField(
                related_name="user_like", to="products.product"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
