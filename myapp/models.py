from django.db import models
import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserManager(BaseUserManager):
    # ユーザー作成のためのやつ
    def _create_user(self, username, password, **extra_fields): 
        # ユーザーネームがなかったらエラー
        if not username: 
            raise ValueError('username is requied')

        user = self.model(username=username, **extra_fields) # ユーザーネーム
        user.set_password(password) # パスワード、デフォルトでハッシュになる
        user.save(using=self._db) # トランザクションを終了する
        return user

    # ユーザー作成のためのやつ、adminではないユーザーを保存する _create_user を呼び出して定義
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    # ユーザー作成のためのやつ、adminユーザーを保存する _create_user を呼び出して定義
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)

# ユーザーテーブル
class User(AbstractBaseUser, PermissionsMixin):
    # 不正な文字列が含まれていないかチェックする
    username_validator = UnicodeUsernameValidator()

    # ここから下は通常のテーブル定義を同じ
    username = models.CharField(max_length=150, unique=True, validators=[username_validator])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField( default=datetime.datetime.now)

    # ここで先ほど定義したクラスを呼び出してデフォルトのユーザーモデルとして定義する
    objects = UserManager()

    # ユーザーネームと必須のフィールドを定義する、ここは重複禁止
    # 重複する場合は REQUIRED_FIELDS はからの配列を渡せば良い
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []