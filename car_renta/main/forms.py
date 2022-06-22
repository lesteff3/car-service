from django.forms import ModelForm, Select, DateInput, TextInput
from .models import OrderItems


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
