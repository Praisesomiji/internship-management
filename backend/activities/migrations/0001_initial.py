# Generated by Django 4.2.14 on 2024-07-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('teams', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('cost_in_naira', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('loss_or_mortality', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.production')),
            ],
        ),
        migrations.CreateModel(
            name='Trace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.profile')),
                ('productions', models.ManyToManyField(to='products.production')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.team')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('activities', models.ManyToManyField(to='activities.activity')),
            ],
        ),
    ]