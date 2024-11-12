from django import forms 
from .models import Post

# Suggested code may be subject to a license. Learn more: ~LicenseLog:211307071.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 
            'content'
            ]