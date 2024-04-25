from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils import timezone


class User_report(models.Model):

    PRIORITY_CHOICES = [
        ('H', 'Высокий'),
        ('A', 'Средний'),
        ('L', 'Низкий')
    ]

    SERIOUSNESS_CHOICES = [
        ('S1', 'Блокирующая'),
        ('S2', 'Критическая'),
        ('S3', 'Значительная'),
        ('S4', 'Незначительная'),
        ('S5', 'Тривиальная')
    ]

    STATUS_CHOICES = [
        ('O', 'Открыто'),
        ('W', 'В работе'),
        ('T', 'Тестирование'),
        ('D', 'Выполнено'),
    ]

    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField ('Статуc', max_length=1, choices=STATUS_CHOICES, default='O', blank=False)
    title = models.CharField('Заголовок',max_length=100, blank=False)
    priority = models.CharField('Приоритет',max_length=1, choices=PRIORITY_CHOICES, default='L', blank=False)
    seriousness = models.CharField('Серьезность бага', max_length=2, choices=SERIOUSNESS_CHOICES, default='S5', blank=False)
    description = models.CharField('Описание',max_length=250, blank=False)
    playback_steps = models.TextField('Шаги воспроизведения',max_length=250, blank=False)
    actual_result = models.CharField('Фактический результат', max_length=250, blank=False)
    expected_result = models.CharField('Ожидаемый результат', max_length=250, blank=False)
    context = models.CharField('Окружение', max_length=150, blank=False)
    attachments = models.ImageField('Вложения', upload_to='images/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    more_information = models.TextField('Дополнительная информация', max_length=250, blank=False)
    file = models.FileField('Файл лога', upload_to='uploads/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['log']), MaxLengthValidator(1*1024*1024)])
    created_at = models.DateTimeField('Дата и время создания', default=timezone.now)  # Время создания

    @staticmethod
    def get_default_user():
        user = User.objects.first()
        return user.id if user else 1


    def get_url(self):
        try:
            return reverse('one_bug_report', kwargs={'pk_bug_report': self.pk})
        except NoReverseMatch:
            # Обработка случаев, когда URL не может быть сгенерирован
            return None


    def __str__(self):
        return f'{self.user} - {self.status} {self.title} {self.priority} {self.seriousness} {self.description}'


    class Meta:
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = ('Сообщения от пользователей')


default_user_id = User_report.get_default_user()


