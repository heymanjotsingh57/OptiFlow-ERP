from django import forms
import re
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            "customer_name",
            "phone_number",
            "address",
            "age",
            "gender",

            "doctor_name",

            "frame_details",
            "frame_price",
            "lens_details",
            "lens_price",

            "right_eye_sph",
            "right_eye_cyl",
            "right_eye_axis",

            "left_eye_sph",
            "left_eye_cyl",
            "left_eye_axis",

            "pd",

            "gst",
            "discount",
            "advance_paid",

            "delivery_date",

            "remarks",

            "status",
        ]

        widgets = {

            "customer_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter customer name"
            }),

            "phone_number": forms.TextInput(attrs={
    "class": "form-control",
    "placeholder": "Enter 10 digit mobile number",
    "maxlength": "10",
    "inputmode": "numeric",
    "pattern": "[6-9]{1}[0-9]{9}",
    "title": "Enter a valid 10 digit Indian mobile number",
    "autocomplete": "off"
}),

            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "gender": forms.Select(attrs={
                "class": "form-select"
            }),

            "doctor_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "frame_details": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "frame_price": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "lens_details": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "lens_price": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "right_eye_sph": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "right_eye_cyl": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "right_eye_axis": forms.TextInput(attrs={
                "class": "form-control"
            }),            "left_eye_sph": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "left_eye_cyl": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "left_eye_axis": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "pd": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "PD (Pupillary Distance)"
            }),

            "gst": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "GST %"
            }),

            "discount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Discount"
            }),

            "advance_paid": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Advance Paid"
            }),

            "delivery_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

        }

    def clean_phone_number(self):

        phone = self.cleaned_data["phone_number"].strip()

        if not re.fullmatch(r"[6-9]\d{9}", phone):
            raise forms.ValidationError(
                "Enter a valid 10 digit Indian mobile number."
            )

        return phone