from django import forms
from GamesPlayApp.car.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'priority', 'image_url', 'summary']
        labels = {
            'image_url': 'Image URL',
            'priority': 'Height'
        }


class CarDeleteForm(CarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
