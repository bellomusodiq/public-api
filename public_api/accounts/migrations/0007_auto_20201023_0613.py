# Generated by Django 3.1.2 on 2020-10-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_transaction_trade_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trade_date_limit',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trade_effective_date',
            field=models.CharField(max_length=100),
        ),
    ]
