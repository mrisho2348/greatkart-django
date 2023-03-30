from django import forms 
from .models import ReviewRating
class ReviewForm(forms.ModelForm):
    model = ReviewRating
    fields = ['subject','review','rating']