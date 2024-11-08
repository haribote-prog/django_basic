import os

from django import forms
from django.core.mail import EmailMessage


class InquiryForm(forms.Form):
    name = forms.CharField(label="お名前", max_length=30)
    email = forms.EmailField(label="メールアドレス")
    title = forms.CharField(label="タイトル", max_length=30)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["placeholder"] = "お名前をここに入力してください．"

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        title = self.cleaned_data["title"]
        message = self.cleaned_data["message"]

        subject = f"お問い合わせ {title}"
        body = f"送信者名：{name}\nメールアドレス：{email}\nメッセージ：{message}"
        from_email = os.environ.get("FROM_EMAIL")
        to_list = [os.environ.get("FROM_EMAIL")]
        cc_list = [email]

        msg = EmailMessage(subject=subject, body=body, from_email=from_email, to=to_list, cc=cc_list)
        msg.send()
