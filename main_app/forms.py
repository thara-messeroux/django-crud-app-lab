from django import forms
from .models import Discovery


class DiscoveryForm(forms.ModelForm):
    # Creates a clean form for adding and editing trail discoveries.
    class Meta:
        model = Discovery

        # User is excluded because Django sets the owner automatically.
        fields = [
            'title',
            'category',
            'tags',
            'location',
            'date_seen',
            'description',
            'safety_tip',
            'preservation_tip',
            'image_url',
            'image_upload',
        ]

        widgets = {
            # Uses checkboxes because tags are flexible multi-select labels.
            'tags': forms.CheckboxSelectMultiple,

            # Uses a friendly date picker in modern browsers.
            'date_seen': forms.DateInput(attrs={'type': 'date'}),

            # Makes longer writing areas easier to use.
            'description': forms.Textarea(attrs={'rows': 4}),
            'safety_tip': forms.Textarea(attrs={'rows': 3}),
            'preservation_tip': forms.Textarea(attrs={'rows': 3}),
        }
