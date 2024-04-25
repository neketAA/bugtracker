# Generated by Django 4.2.11 on 2024-04-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_report', '0003_rename_user_id_user_report_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_report',
            name='actual_result',
            field=models.CharField(max_length=250, verbose_name='Фактический результат'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='context',
            field=models.CharField(max_length=150, verbose_name='Окружение'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='expected_result',
            field=models.CharField(max_length=250, verbose_name='Ожидаемый результат'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='more_information',
            field=models.TextField(max_length=250, verbose_name='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='playback_steps',
            field=models.TextField(max_length=250, verbose_name='Шаги воспроизведения'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='priority',
            field=models.CharField(choices=[('H', 'Высокий'), ('A', 'Средний'), ('L', 'Низкий')], default='L', max_length=1, verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='seriousness',
            field=models.CharField(choices=[('S1', 'Блокирующая'), ('S2', 'Критическая'), ('S3', 'Значительная'), ('S4', 'Незначительная'), ('S5', 'Тривиальная')], default='S5', max_length=2, verbose_name='Серьезность бага'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='status',
            field=models.CharField(choices=[('O', 'Открыто'), ('W', 'В работе'), ('T', 'Тестирование'), ('D', 'Выполнено')], default='O', max_length=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='user_report',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]