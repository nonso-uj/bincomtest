from django import forms
from .models import PollingUnit


class PollResultForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['polling_unit_id'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['ward_id'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['lga_id'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['uniquewardid'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['polling_unit_number'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['polling_unit_name'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['polling_unit_description'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3 
            })
        self.fields['lat'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['long'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['entered_by_user'].widget.attrs.update({
            'class': 'form-control', 
            })
        self.fields['user_ip_address'].widget.attrs.update({
            'class': 'form-control', 
            })

    class Meta:
        model = PollingUnit
        fields = '__all__'
        exclude = ['uniqueid', 'date_entered']