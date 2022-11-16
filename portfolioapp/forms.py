from django import forms
from django.conf import settings
from django.core.mail import send_mail



class ContactForm(forms.Form):

    name = forms.CharField(max_length=120, 
        widget=forms.TextInput(attrs={'placeholder': 'Your Full Name..', 'class':'form-control'}))
    phone = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'placeholder': 'Your Phone No...','class':'form-control' }))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'placeholder': 'Your email address..', 'class':'form-control'}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Your subject..', 'class':'form-control'}))
   
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message..','class':'form-control', 'col':'3'}))

    
    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
       
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )