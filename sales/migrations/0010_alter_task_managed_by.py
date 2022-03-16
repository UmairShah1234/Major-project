# Generated by Django 4.0.2 on 2022-03-16 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0009_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='managed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lead_user', to=settings.AUTH_USER_MODEL),
        ),
    ]