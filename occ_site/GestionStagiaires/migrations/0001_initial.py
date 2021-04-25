# Generated by Django 3.1.7 on 2021-03-25 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=200)),
                ('msg', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_direction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Encadreur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_encad', models.CharField(max_length=20)),
                ('postnom_encad', models.CharField(max_length=20)),
                ('prenom_encad', models.CharField(max_length=20)),
                ('sexe_encad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_stagiaire', models.CharField(max_length=20)),
                ('postnom_stagiaire', models.CharField(max_length=20)),
                ('prenom_stagiaire', models.CharField(max_length=20)),
                ('sexe_stagiaire', models.CharField(max_length=10)),
                ('email_stagiaire', models.EmailField(max_length=200)),
                ('adresse_stagiaire', models.CharField(max_length=200)),
                ('telephone_stagiaire', models.CharField(max_length=15)),
                ('type_stage', models.CharField(max_length=20)),
                ('promotion_stagiaire', models.CharField(max_length=20)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='directions', to='GestionStagiaires.direction')),
                ('encadreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encadreurs', to='GestionStagiaires.encadreur')),
            ],
        ),
    ]
