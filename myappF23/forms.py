from django import forms
from myappF23.models import Order


class InterestForm(forms.Form):
    CHOICES = [
        ('1', 'Yes'),
        ('0', 'No'),
    ]
    interested= forms.ChoiceField(required=True, widget=forms.RadioSelect(
    attrs={'class': 'Radio'}), choices=CHOICES)
    levels=forms.IntegerField(min_value=1,max_value=5, initial=1)
    comments= forms.CharField(widget=forms.Textarea,label="Additional Comments")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["student", "course", "levels", "order_date"]

        widget={
            'student': forms.ChoiceField(widget=forms.RadioSelect())
        }