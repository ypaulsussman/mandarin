# Generated by Django 3.2.8 on 2021-10-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chengyu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('z_rarity', models.IntegerField(choices=[{1, 'Very Common'}, {2, 'Common'}, {'Uncommon', 3}, {4, 'Rare'}, {'Very Rare', 5}], default=3)),
                ('demo_sentence_zh', models.CharField(max_length=500)),
                ('demo_sentence_pn', models.CharField(max_length=500)),
                ('demo_sentence_en', models.CharField(max_length=500)),
            ],
        ),
    ]
