# Generated by Django 3.2 on 2021-05-19 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('points', models.SmallIntegerField(verbose_name='points')),
                ('difficulty', models.IntegerField(choices=[(0, 'Any'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], default=0, verbose_name='Difficulty')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('question_type', models.IntegerField(choices=[(0, 'Multiple Choice'), (1, 'True/False')], default=0, verbose_name='Question Type')),
                ('is_for_exam', models.BooleanField(default=False, verbose_name='Is For Exam')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('quiz', models.ManyToManyField(blank=True, to='quiz.Quiz')),
                ('subcategories', models.ManyToManyField(to='quiz.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct Answer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='question.question', verbose_name='Question')),
            ],
        ),
    ]
