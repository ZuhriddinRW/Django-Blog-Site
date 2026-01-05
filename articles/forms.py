from django import forms
from .models import Comment


class CommentForm ( forms.ModelForm ) :
    comment = forms.CharField (
        max_length=800,
        widget=forms.Textarea (
            attrs={
                "rows" : 4,
                "placeholder" : "Write a comment...",
            }
        ),
        label="",
    )

    class Meta :
        model = Comment
        fields = ["comment"]