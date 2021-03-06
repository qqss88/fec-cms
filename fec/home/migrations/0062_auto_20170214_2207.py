# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_merge_20170210_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipsfortreasurerspage',
            name='read_next',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.TipsForTreasurersPage'),
        ),
        migrations.AlterField(
            model_name='documentfeedpage',
            name='category',
            field=models.CharField(choices=[('oig', 'oig'), ('strategy_budget_performance', 'strategy budget performance'), ('foia', 'foia'), ('privacy', 'privacy'), ('procurement_contracting_reports', 'procurement contracting reports'), ('annual_anniversary', 'annual anniversary'), ('agency_operations', 'agency operations')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='documentpage',
            name='category',
            field=models.CharField(choices=[('audit report', 'Audit report'), ('inspection report', 'Inspection report'), ('special review report', 'Special review report'), ('semiannual report', 'Semiannual report'), ('strategic plan', 'Strategic plan'), ('it strategic plan', 'IT strategic plan'), ('congressional budget justification', 'Congressional budget justification'), ('annual performance report', 'Annual performance report'), ('performance and accountability report', 'Performance and accountability report'), ('annual foia report', 'Annual FOIA report'), ('privacy act notices', 'Privacy Act notices'), ('privacy policy', 'Privacy policy'), ('purchase inventory', 'Purchase inventory'), ('annual report', 'Annual report'), ('fair act inventory report', 'FAIR Act inventory report'), ('request for proposal (rfp)', 'Request for proposal (RFP)'), ('anniversary report', 'Anniversary report'), ('shutdown plan', 'Shutdown plan'), ('operation plan', 'Operation plan')], max_length=255, null=True),
        ),
    ]
