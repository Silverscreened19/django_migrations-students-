# Generated by Django 4.1.7 on 2023-03-17 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]
