from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from GamesPlayApp.profile_car.models import Profile


class ProfileForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username'
            }
        )
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password'
            }
        )
    )


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['email', 'age', 'password']
#
#         widgets = {
#             'password': forms.PasswordInput()
#         }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'username', 'profile_picture']
        exclude = ['password']
