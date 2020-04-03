# Generated by Django 3.0.4 on 2020-04-03 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_edit_time', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField(max_length=500)),
                ('location', models.TextField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.SmallIntegerField(choices=[(1, 'invited you to attend'), (2, 'has accepted your invite to'), (3, 'cannot attend'), (4, 'sent you a personal message regarding '), (5, 'cancelled the event')], null=True)),
                ('message', models.TextField(max_length=500)),
                ('decision_time', models.DateTimeField(auto_now=True)),
                ('meeting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.Meeting')),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
