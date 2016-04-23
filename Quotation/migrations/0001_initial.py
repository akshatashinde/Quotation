# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=b'0')),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.CharField(max_length=200)),
                ('quotation_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='quotation_no',
            field=models.ForeignKey(blank=True, to='Quotation.Quotation', null=True),
        ),
    ]
