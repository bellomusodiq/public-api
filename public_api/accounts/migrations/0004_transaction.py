# Generated by Django 3.1.2 on 2020-10-23 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20201020_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_ref', models.CharField(max_length=400)),
                ('cscs_number', models.CharField(max_length=100)),
                ('instructions', models.CharField(max_length=400)),
                ('trade_date_limit', models.DateField()),
                ('trade_effective_date', models.DateField()),
                ('trade_action', models.CharField(max_length=100)),
                ('trade_price_limit', models.CharField(max_length=400)),
                ('trade_unit', models.CharField(max_length=400)),
                ('sms_pin', models.BigIntegerField(blank=True, null=True)),
                ('stock_code', models.CharField(max_length=100)),
                ('trade_account_type', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]