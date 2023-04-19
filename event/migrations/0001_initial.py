# Generated by Django 4.2 on 2023-04-14 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('event_status', models.BooleanField(default=False)),
                ('attendees', models.PositiveBigIntegerField()),
                ('event_date', models.DateTimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
