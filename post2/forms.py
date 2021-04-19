from django import forms
from .models import Post2

class Post2Form(forms.ModelForm):
    
    shows = forms.CharField(required=False)

    class Meta:
        model = Post2
        fields = [
                'shows',
        ]
        

