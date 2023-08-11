from django import forms
from GamesPlayApp.events.models import Event, EventGalleryImage


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'time', 'location', 'image_url', 'description']
        labels = {
            'image_url': 'Image URL'
        }
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'time': forms.DateInput(attrs={'placeholder': 'HH:MM'}),
        }


class EventDeleteForm(EventForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'

class EventGalleryImageForm(forms.ModelForm):
    class Meta:
        model = EventGalleryImage
        fields = ['image_url']

        labels = {
            'image_url': 'Image URL'
        }

class UserReviewForm(forms.Form):
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        label='Rating'
    )
    review_text = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3}),
        label='Review'
    )