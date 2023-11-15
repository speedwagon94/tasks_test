from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Обработчик сигнала для автоматического создания токена аутентификации при создании пользователя.

    Parameters:
    - sender: Модель, отправившая сигнал (в данном случае, User).
    - instance: Экземпляр модели, который был сохранен.
    - created (bool): Флаг, указывающий, был ли объект только что создан.

    Notes:
    - Эта функция связывается с сигналом post_save и автоматически вызывается каждый раз, когда объект User сохраняется.
    - Если объект User был только что создан (created=True), создается токен аутентификации и привязывается к пользователю.
    """
    if created:
        Token.objects.create(user=instance)