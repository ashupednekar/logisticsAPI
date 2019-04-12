from rest_framework import serializers

from .models import Features

class FeatureSerializer(serializers.ModelSerializer):

    class Meta():
        model = Features
        fields = ('vol_outscan', 'vol_del', 'ppd_Vol', 'ppd_Delv_Vol', 'cod_Vol', 'cod_Delv_Vol', 'RTS_Vol', 'RTS_Delv_Vol', 'EDS_Vol', 'EDS_Pickup_Completed', 'RVP_Pickup_Vol', 'RVP_Pickup_Completed', 'RVP_Outscan_Vol', 'RVP_Delv_Vol', 'weight', 'Amazon', 'Flipkart', 'Club_Factory', 'Paytm', 'Myntra', 'Snap_Deal', 'others', 'FE_Type', 'Voucher_Number', 'Total_Km', 'fuel_exp', 'Fuel_Expenses_Reimbursed')