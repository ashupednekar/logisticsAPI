# Generated by Django 2.2 on 2019-04-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190411_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='features',
            name='lname',
        ),
        migrations.AddField(
            model_name='features',
            name='Amazon',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Club_Factory',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='EDS_Pickup_Completed',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='EDS_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='FE_Type',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Flipkart',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Fuel_Expenses_Reimbursed',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Myntra',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Paytm',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='RTS_Delv_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='RTS_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='RVP_Delv_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='RVP_Outscan_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='RVP_Pickup_Completed',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='RVP_Pickup_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Snap_Deal',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Total_Km',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='Voucher_Number',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='cod_Delv_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='cod_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='fuel_exp',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='others',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='ppd_Delv_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='ppd_Vol',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='vol_del',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='vol_outscan',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='features',
            name='weight',
            field=models.FloatField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
