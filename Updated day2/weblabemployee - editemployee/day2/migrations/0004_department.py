# Generated by Django 3.1.3 on 2022-12-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day2', '0003_remove_employee_id_employee_registration_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=255)),
            ],
        ),
    ]