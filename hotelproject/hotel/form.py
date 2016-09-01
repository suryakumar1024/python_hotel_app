from django import forms


class HotelDetails(forms.Form):
    hotel_name = forms.CharField(max_length=100)
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))


class MenuCard(forms.Form):
    item_one = forms.CharField(max_length=100)
    item_two = forms.CharField(max_length=100)
