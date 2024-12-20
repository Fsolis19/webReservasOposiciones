from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from .models import Customer, ShippingAddress, Course
from django.core.validators import MinLengthValidator, RegexValidator, MaxValueValidator, MinValueValidator

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), required=True)

class RegisterForm(forms.Form):
    name = forms.CharField(label='Nombre Completo', required=True)
    email = forms.EmailField(label='Correo Electrónico', required=True)
    adress = forms.CharField(label='Dirección', max_length=200, required=True)
    phone = forms.IntegerField(label='Teléfono', validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = get_user_model().objects.filter(email=email)
        if qs.exists():
            self.add_error('email', 'El correo electrónico ya está registrado')
        try:
            validate_email(email)
        except:
            self.add_error('email', 'El correo electrónico no es válido')
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            self.add_error('password', 'La contraseña debe tener al menos 8 caracteres')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2 and password != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')
    
    
    def save(self, commit=True):
        user = get_user_model().objects.create_user(
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
        return user

class CustumerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'adress', 'phone']
        labels = {
            'name': 'Nombre',
            'email': 'Correo',
            'adress': 'Dirección',
            'phone': 'Teléfono'
        }
    name = forms.CharField(label='Nombre Completo', required=True)
    email = forms.EmailField(label='Correo Electrónico', required=True)
    adress = forms.CharField(label='Dirección', max_length=200, required=True)
    phone = forms.IntegerField(label='Teléfono', validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
        labels = {
            'name': 'Nombre',
            'email': 'Correo'
        }
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ShippingAddressForm(forms.ModelForm):
    zipcode = forms.CharField(label='Código Postal',
    validators=[RegexValidator(r'^\d{5}$', 'El código postal debe contener exactamente 5 dígitos.')])
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'zipcode', 'country']
        labels = {
            'address': 'Dirección',
            'city': 'Ciudad',
            'state': 'Comunidad Autónoma',
            'country': 'País',
        }

    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name', 'image', 'price', 'details', 
            'city', 'course_type', 'is_available', 'capacity',
            'start_date', 'end_date'
        ]
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            'price': 'Precio',
            'details': 'Detalles',
            'city': 'Ciudad',
            'course_type': 'Tipo del curso',
            'is_available': 'Disponibilidad',
            'capacity': 'Capacidad',
            'start_date': 'Fecha de comienzo',
            'end_date': 'Fecha final',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name', 'image', 'price', 'details', 
            'city', 'course_type', 'is_available', 'capacity',
            'start_date', 'end_date'
        ]
        labels = {
            'name': 'Nombre',
            'image': 'Imagen',
            'price': 'Precio',
            'details': 'Detalles',
            'city': 'Ciudad',
            'course_type': 'Tipo del curso',
            'is_available': 'Disponibilidad',
            'capacity': 'Capacidad',
            'start_date': 'Fecha de comienzo',
            'end_date': 'Fecha final',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }