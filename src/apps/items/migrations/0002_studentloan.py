# Generated by Django 5.0.7 on 2024-08-01 04:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('users', '0005_alter_student_academic_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='quantidade')),
                ('date_of_loan', models.DateField(verbose_name='data do empréstimo')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='data da devolução')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.item', verbose_name='item')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.student', verbose_name='aluno')),
            ],
            options={
                'verbose_name': 'Empréstimo de estudante',
                'verbose_name_plural': 'Empréstimos de estudantes',
            },
        ),
    ]