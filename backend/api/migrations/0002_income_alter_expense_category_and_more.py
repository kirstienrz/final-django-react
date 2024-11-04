# Generated by Django 5.1.2 on 2024-11-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('source', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
