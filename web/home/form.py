from django import  forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Post
class DangKy(forms.Form):
    username =forms.CharField(label='Tài khoản',max_length=30)
    password1 =forms.CharField(label='Mật khẩu',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
         password1= self.cleaned_data['password1']
         password2 = self.cleaned_data['password2']
        if password1==password2 and password1:
            return password2
        raise forms.ValidationError('Mat Khau khong hop le')
    def clean_username(self):
        username= self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Tai khoan co ky tu dac biet')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
                return username
        raise forms.ValidationError('Tai khoan da ton tai')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email=None,password=self.cleaned_data['password1'])

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','image')
        # title = forms.CharField(label='Tiêu đề:',max_length=30)
        # content=forms.CharField(label='Mô tả:')
        # # user= User()
        # # author=user.username
        # image = forms.FileField()
        #
        # def save(self):
        #      a=Post()
        #      a.title=self.title
        #      a.content=self.content
        #      a.author=self.author
        #      a.image=self.image

