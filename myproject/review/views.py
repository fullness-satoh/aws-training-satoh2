from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Product
from .models import Review

class ReviewTopView(TemplateView):
    template_name = 'review/review-top.html'

class ProductListView(ListView):
    template_name = "review/product-list.html"
    model = Product
    context_object_name = "products"

class ReviewListView(ListView):
    # 表示するページのhtmlを指定
    template_name = "review/review-list.html"
    # modelの指定
    model = Review
    # review リストを object_list に格納
    object_list = "reviews"

class ProductDetailView(DetailView):
    template_name = "review/product-detail.html"
    model = Product

class ReviewDetailView(DetailView):
    template_name = "review/review-detail.html"
    model = Review

class CreateReviewView(LoginRequiredMixin, CreateView):
    template_name = "review/create-review.html"
    model = Review
    fields = ['product', 'rating', 'comment']  # 必要なフィールドを指定

    # 成功時のリダイレクトURLを動的に生成するメソッド
    def get_success_url(self):
            # レビューの詳細ページへのURLを生成
            return reverse_lazy('review:review-detail', kwargs={'pk': self.object.pk})

    # form_valid関数を追加
    def form_valid(self, form):
        form.instance.user = self.request.user  # 現在のログインユーザーを user フィールドに設定
        return super().form_valid(form)


class UpdateReviewView(LoginRequiredMixin, UpdateView):
    template_name = "review/update-review.html"
    model = Review
    fields = ['product', 'rating', 'comment']    # 必要なフィールドを指定

    # 成功時のリダイレクトURLを動的に生成するメソッド
    def get_success_url(self):
            # レビューの詳細ページへのURLを生成
            return reverse_lazy('review:review-detail', kwargs={'pk': self.object.pk})

    # form_valid関数を追加
    def form_valid(self, form):
        form.instance.user = self.request.user  # 現在のログインユーザーを user フィールドに設定
        return super().form_valid(form)

class DeleteReviewView(LoginRequiredMixin, DeleteView):
    template_name = "review/delete-review.html"
    model = Review
    # 削除後は、レビュー一覧ページへ
    success_url = reverse_lazy('review:review-list')
