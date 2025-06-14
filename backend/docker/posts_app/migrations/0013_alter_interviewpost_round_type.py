# Generated by Django 5.2 on 2025-04-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0012_alter_interviewpost_round_type_alter_post_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewpost',
            name='round_type',
            field=models.CharField(choices=[('application', 'Application'), ('online_assessment', 'Online Assessment'), ('technical_interview', 'Technical Interview'), ('behavioral', 'Behavioral Interview'), ('system_design', 'System Design'), ('hr_interview', 'HR Interview'), ('team_match', 'Team Match')], max_length=30),
        ),
    ]
