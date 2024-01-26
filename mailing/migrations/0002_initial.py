
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingsettings',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mail',
            name='client_to_message',
            field=models.ManyToManyField(blank=True, null=True, related_name='client_to_message', to='client.mailingclient', verbose_name='Клиенты'),
        ),
        migrations.AddField(
            model_name='mail',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings'),
        ),
    ]
