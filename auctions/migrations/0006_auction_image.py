# Generated by Django 5.0.2 on 2024-02-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_remove_auction_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="auction",
            name="image",
            field=models.URLField(blank=True),
        ),
    ]