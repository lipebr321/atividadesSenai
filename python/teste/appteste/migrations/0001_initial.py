# Generated by Django 5.0.2 on 2024-02-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pessoas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('email', models.TextField()),
                ('telefone', models.IntegerField()),
                ('mensagem', models.TextField()),
            ],
        ),
    ]
