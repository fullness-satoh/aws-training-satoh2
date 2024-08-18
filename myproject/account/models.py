from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUserを継承
class Account(AbstractUser):
    # 必要に応じてフィールドを追加
    pass

