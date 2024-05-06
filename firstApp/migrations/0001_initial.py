# Generated by Django 5.0.4 on 2024-05-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vender_Model',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('vender_code', models.IntegerField(primary_key=True, serialize=False)),
                ('quality_rating_avg', models.FloatField(max_length=5)),
                ('average_response_time', models.FloatField(max_length=60)),
                ('fulfillment_rate', models.FloatField(max_length=100)),
            ],
        ),
    ]
