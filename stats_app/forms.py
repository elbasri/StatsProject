# stats_app/forms.py
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    algorithme = forms.MultipleChoiceField(
        choices=[
            ('topProd', 'topProd'),
            ('visualiser', 'Visualiser'),
            ('mounthlyRev', 'mounthlyRev'),
            ('GradientDescent', 'Gradient descent'),
            ('NormalizeMinMax', 'Normalizer(MinMax)'),
            ('MseN', 'MSE (Normalized)'),
            ('GradientDescentN', 'Gradient descent (Normalized)')
        ],
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    externe = forms.Field()