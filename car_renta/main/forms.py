from django.forms import ModelForm, Select, DateInput, TextInput, Textarea

from .models import OrderItems, Review


class OrderItemsForm(ModelForm):
    class Meta:
        model = OrderItems

        fields = ['product', 'color', 'phone', 'created_at']

        widgets = {
            "product": Select(attrs={
                'class': 'form-control',
            }),
            "color": Select(attrs={
                'class': 'form-control',
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: +375445865118'
            }),
            "created_at": DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review

        fields = ['user', 'text']

        widgets = {
            "user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Иванов Иван Иванович'
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв'
            }),
        }