
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_subject', models.CharField(max_length=255, verbose_name='тема письма')),
                ('mailing_body', models.CharField(max_length=500, verbose_name='тело письма')),
                ('all_clients', models.BooleanField(blank=True, null=True, verbose_name='все клиенты')),
                ('is_active', models.BooleanField(default=True, verbose_name='активный')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_status', models.CharField(choices=[('AC', 'Active'), ('FI', 'Finished'), ('CR', 'Created')], default='CR', max_length=2, verbose_name='статус рассылки')),
                ('mailing_time_start', models.DateTimeField(blank=True, null=True, verbose_name='время начала рассылки')),
                ('mailing_time_end', models.DateTimeField(blank=True, null=True, verbose_name='время конца рассылки')),
                ('mailing_periods', models.CharField(choices=[('DL', 'Daily'), ('WL', 'Weekly'), ('ML', 'Monthly')], max_length=2, verbose_name='периодичность')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылки',
                'ordering': ['mailing_status'],
            },
        ),
        migrations.CreateModel(
            name='MailingTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_try', models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')),
                ('mailing_try_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='статус рассылки')),
                ('mailing_response', models.CharField(blank=True, max_length=255, null=True, verbose_name='ответ почтового сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
