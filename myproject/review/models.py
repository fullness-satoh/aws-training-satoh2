from django.db import models
from account.models import Account
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# 商品モデル
class Product(models.Model):
    # 商品名
    name = models.CharField(max_length=255)  # 最大255文字の文字列フィールド
    # 商品説明
    description = models.TextField(blank=True, null=True)  # フォームで空白可、データベースでNULL値可
    # 商品価格
    price = models.IntegerField()  # 整数フィールド
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)  # 作成時に自動的に現在の日時が設定される
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新時に自動的に現在の日時が設定される

    def __str__(self):
        return self.name  # オブジェクトを文字列として表示する際に商品名を返す

# レビューモデル
class Review(models.Model):
    # レビュータイトル
    title = models.CharField(max_length=255)  # 最大255文字の文字列フィールド
    # ユーザー
    user = models.ForeignKey(Account, on_delete=models.CASCADE)  # カスタムユーザーモデルとの外部キー
    # 商品
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 商品モデルとの外部キー
    # 評価
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # 1から5の範囲に制限
    # コメント
    comment = models.TextField(blank=True, null=True)  # フォームで空白可、データベースでNULL値可
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)  # 作成時に自動的に現在の日時が設定される
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新時に自動的に現在の日時が設定される

    def __str__(self):
        return self.title  # オブジェクトを文字列として表示する際に商品名を返す


