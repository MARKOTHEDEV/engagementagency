# Generated by Django 4.0.4 on 2022-05-06 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_quiz_result_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='result',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
