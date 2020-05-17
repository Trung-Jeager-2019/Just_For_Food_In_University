from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=100, required=True)
    contact_email = forms.EmailField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

    def __str__(seft):
        return seft.contact_name + "-" + seft.contact_name + ":" + seft.content
