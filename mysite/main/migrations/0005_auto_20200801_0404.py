# Generated by Django 3.0.8 on 2020-07-31 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200731_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='coupon_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pateint_ph',
            field=models.CharField(max_length=10),
        ),
    ]
