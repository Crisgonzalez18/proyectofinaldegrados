from django import forms
class FormularioPaciente(forms.Form):

    TipoAfiliado=(
        (1,'Cotizante'),
        (2,'Beneficiario'),
    )
    Regimen=(
        (1,'Excepcion'),
        (2, 'Especial'),
        (3, 'Controbutivo'),
        (4, 'Subsidiado'),
        (5, 'No Asegurado'),
        (6, 'Indeterminado / Pendiente')
    )
    GrupoIngreso=(
        (1,'A MENOR A 2 SMMLV'),
        (2,'B ENTRE 2 Y 4 SMMLV'),
        (3,'C MAS DE 5 SMMLV')
    )

    nombre=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    ) 
    apellidos=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedula=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10
    )
    TipoAfiliado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=TipoAfiliado
    )
    regimen=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=Regimen
    )
    contacto=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=20
    )
    GrupoIngreso =forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-3"}),
        required=True,
        choices=GrupoIngreso
    ) 