from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254, unique=True, verbose_name='контактный email')),
                ('first_name', models.CharField(max_length=25, verbose_name='имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='фамилия')),
                ('surname', models.CharField(blank=True, max_length=25, null=True, verbose_name='отчество')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарии')),
            ],
            options={
                'verbose_name': 'Клиент рассылки',
                'verbose_name_plural': 'Клиенты рассылок',
            },
        ),
    ]
