# Generated by Django 3.0.3 on 2020-05-15 02:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pagos', '0002_auto_20200514_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_p', to=settings.AUTH_USER_MODEL),
        ),
    ]
