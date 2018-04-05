from django import forms

class CommentForm (forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName', 'placeholder': 'Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'comment', 'placeholder': 'Comment', 'rows':5}))