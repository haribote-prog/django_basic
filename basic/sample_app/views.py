import logging
from typing import Any

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import DiaryCreateForm, InquiryForm
from .models import Diary

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("sample_app:inquiry")

    def form_valid(self, form: InquiryForm) -> HttpResponse:
        form.send_email()
        messages.success(self.request, "メッセージを送信しました．")
        logger.info(f"Inquiry sent by {form.cleaned_data["name"]}")
        return super().form_valid(form)


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = "diary_list.html"
    paginate_by = 2

    def get_queryset(self) -> QuerySet[Any]:
        diaries = Diary.objects.filter(user=self.request.user).order_by("-created_at")
        return diaries


class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = "diary_detail.html"


class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = "diary_create.html"
    form_class = DiaryCreateForm
    success_url = reverse_lazy("sample_app:diary_list")

    def form_valid(self, form: DiaryCreateForm) -> HttpResponse:
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, "日記を作成しました")
        return super().form_valid(form)

    def form_invalid(self, form: DiaryCreateForm) -> HttpResponse:
        messages.error(self.request, "日記の作成に失敗しました")
        return super().form_invalid(form)


class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Diary
    template_name = "diary_update.html"
    form_class = DiaryCreateForm

    def get_success_url(self) -> str:
        return reverse_lazy("sample_app:diary_detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form: DiaryCreateForm) -> HttpResponse:
        messages.success(self.request, "日記を更新しました")
        return super().form_valid(form)

    def form_invalid(self, form: DiaryCreateForm) -> HttpResponse:
        messages.error(self.request, "日記の更新に失敗しました")
        return super().form_invalid(form)


class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = "diary_delete.html"
    success_url = reverse_lazy("sample_app:diary_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました")
        return super().delete(request, *args, **kwargs)
