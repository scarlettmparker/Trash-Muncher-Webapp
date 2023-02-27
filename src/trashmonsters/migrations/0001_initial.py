# Generated by Django 4.1.7 on 2023-02-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TrashMonsters",
            fields=[
                ("TM_ID", models.AutoField(primary_key=True, serialize=False)),
                ("Latitude", models.FloatField()),
                ("Longitude", models.FloatField()),
                ("Team1_Score", models.IntegerField(default=0)),
                ("Team2_Score", models.IntegerField(default=0)),
                ("Team3_Score", models.IntegerField(default=0)),
            ],
        ),
    ]