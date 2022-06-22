from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    first_name = forms.CharField(
        label=_('Имя'),
        max_length=100,
        widget=forms.TextInput(attrs={'autocomplete': 'first_name'}),
    )

    last_name = forms.CharField(
        label=_('Фамилия'),
        max_length=100,
        widget=forms.TextInput(attrs={'autocomplete': 'last_name'}),
    )
    phone_numbers = forms.CharField(
        label=_('Номер телефона'),
        max_length=100,
        widget=forms.TextInput(attrs={'autocomplete': 'phone_numbers'}),
    )
    address = forms.CharField(
        label=_('Адрес'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'address', 'placeholder': 'Необязательно'}),
    )
    city = forms.CharField(
        label=_('Город'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'autocomplete': 'city', 'placeholder': 'Необязательно'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_numbers', 'address', 'city')