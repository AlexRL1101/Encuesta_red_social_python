# Generated by Django 4.0.7 on 2022-10-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_correo_alter_employee_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Facebook',
            field=models.CharField(choices=[('', 'Seleccione promedio al día'), ('0', '1 hr'), ('1', '3 hrs'), ('2', '5hrs'), ('3', '6+ hrs')], max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Instagram',
            field=models.CharField(choices=[('', 'Seleccione promedio al día'), ('0', '1 hr'), ('1', '3 hrs'), ('2', '5hrs'), ('3', '6+ hrs')], max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Tiktok',
            field=models.CharField(choices=[('', 'Seleccione promedio al día'), ('0', '1 hr'), ('1', '3 hrs'), ('2', '5hrs'), ('3', '6+ hrs')], max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Twitter',
            field=models.CharField(choices=[('', 'Seleccione promedio al día'), ('0', '1 hr'), ('1', '3 hrs'), ('2', '5hrs'), ('3', '6+ hrs')], max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='WhatsApp',
            field=models.CharField(choices=[('', 'Seleccione promedio al día'), ('0', '1 hr'), ('1', '3 hrs'), ('2', '5hrs'), ('3', '6+ hrs')], max_length=1),
        ),
    ]
