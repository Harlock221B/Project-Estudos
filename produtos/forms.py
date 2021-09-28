from django import forms


class Produto(forms.Form):
    nome = forms.CharField(label='Nome',max_length=50)
    preco = forms.DecimalField( decimal_places=2,max_digits=10, label='Preco')
    quantidade = forms.CharField(label='Quant.')
    obs = forms.CharField(label='Obs', widget=forms.Textarea())
    status = forms.BooleanField(label='Status')
