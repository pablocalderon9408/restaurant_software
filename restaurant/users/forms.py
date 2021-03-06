"""Forms needed for the user: Update personal information, signing up"""
from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""

    first_name = forms.CharField(
        min_length=2, 
        max_length=50,
        label=False,
        widget=forms.TextInput(attrs={'placeholder':'Nombre completo','class': 'form-control','required': True})
    )
    last_name = forms.CharField(
        min_length=2, 
        max_length=50,
        label=False,
        widget=forms.TextInput(attrs={'placeholder':'Apellidos','class': 'form-control','required': True})
        )
        
    username = forms.CharField(
        min_length=4,
        max_length=50,
        label=False,
        widget=forms.TextInput(attrs={'placeholder':'Nombre de usuario','class': 'form-control','required': True})
    )

    password = forms.CharField(
        max_length=70,
        label=False,
        widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class': 'form-control','required': True})
    )

    password_confirmation = forms.CharField(
        max_length=70,
        label= False,
        widget=forms.PasswordInput(attrs={'placeholder':'Confirmar contraseña','class': 'form-control','required': True})
    )

    email = forms.CharField(
        min_length=6,
        max_length=70,
        label=False,
        widget=forms.EmailInput(attrs={'placeholder':'Email','class': 'form-control','required': True})
    )


    #I am getting a Type Error with the country field. It says that User got an unexpexted field. What is needed in order to get the information of this field in the sign up?

    # Error: TypeError at /users/signup/ ----- User() got an unexpected keyword argument 'country'
    #country = forms.CharField(min_length=2, max_length=50)
    #phone_number=forms.CharField(max_length=15)

    # clean() is method that executes to_python(), validate() and run_validators() methods. When you use it, you guarantee that the fields are checked (For example,an integer field must receive an integer. That's the kind of validations that is done by the method). However, to check if an username is already taken or to check the password and password confirmation match, we need to add more logic. Therefore, clean_username sees if the user is already in use, and clean, overrides the clean method (using super()) and do the logic for the password confirmation.

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        #Implement a clean() method on your Form when you must add custom validation for fields that are interdependent. See Cleaning and validating fields that depend on each other for example usage.
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        #Whatever the data submitted with a form, once it has been successfully validated by calling is_valid() (and is_valid() has returned True), the validated form data will be in the form.cleaned_data dictionary. This data will have been nicely converted into Python types for you.
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()