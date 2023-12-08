# Generated by Django 4.2.7 on 2023-12-08 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('Dept_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=100)),
                ('Loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade', models.IntegerField()),
                ('Losal', models.IntegerField()),
                ('Hisal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('Emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Ename', models.CharField(max_length=100)),
                ('Ejob', models.CharField(max_length=100)),
                ('Mgid', models.IntegerField()),
                ('Hiredate', models.DateField()),
                ('Sal', models.IntegerField()),
                ('Comm', models.IntegerField()),
                ('Dept_No', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]