# Generated by Django 4.0.6 on 2022-07-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auction_users_auction_winner_delete_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
