from django import forms

from Ecommerce.orders.models import DeliveryMethodEnum, PaymentMethodEnum


class OrderProfileInformationForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ivan'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ivanov'})
    )
    phone_number = forms.CharField(
        label='Phone Number',
        min_length=13,
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': '+359 888 888 888'}),
    )
    address = forms.CharField(
        label='Address/Office Address',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Sofia, ul.Oborishte #24'})
    )
    city = forms.CharField(
        label='City',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Sofia'})
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.startswith('+'):
            raise forms.ValidationError('Phone number should start with "+".')
        return phone_number


class OrderCommentForm(forms.Form):
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Add Comment Here...'}),
    )


class OrderDeliveryMethodForm(forms.Form):
    CHOICES = DeliveryMethodEnum.get_values()

    delivery_method = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )


class OrderPaymentMethodForm(forms.Form):
    CHOICES = PaymentMethodEnum.get_values()

    payment_method = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )
