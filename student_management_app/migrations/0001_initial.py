# Generated by Django 4.2.3 on 2023-08-13 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_Name', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Name', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Address', models.TextField(max_length=250)),
                ('Mobileno', models.TextField(max_length=12)),
                ('Salary', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Email', models.TextField(max_length=200)),
                ('Date_Of_Birth', models.DateTimeField()),
                ('password', models.TextField(max_length=25)),
                ('Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Naitik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notice_Name', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pos_Name', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('username', models.TextField(max_length=50)),
                ('Email', models.TextField(max_length=200)),
                ('Password', models.TextField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_Name', models.CharField(max_length=80)),
                ('Description', models.TextField(max_length=200)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('Emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.CharField(max_length=200)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('Emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Attandance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Check_in', models.DateTimeField()),
                ('Check_Out', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=50)),
                ('Emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.employee')),
            ],
        ),
    ]