from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Articles
from django.urls import reverse_lazy
# Create your views here.

class ArticlesListView(ListView):
    model = Articles
    template_name = 'articles_list.html'

class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'articles_detail.html'

class ArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')

    # postni chiqargan odam bilan foydalanuvchini tekshirish

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ('title','summary','body','photo',)
    template_name = 'articles_edit.html'

    # postni chiqargan odam bilan foydalanuvchini tekshirish

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticlesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Articles
    fields = ('title','summary','body','photo',)
    template_name = 'articles_new.html'

    # postni chiqargan odam bilan foydalanuvchini tekshirish

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # super user ekanligini tekshirish,
    # admindan boshqa odam post chiqara olmasligi uchun

    def test_func(self):
        return self.request.user.is_superuser