from django import forms
from .models import Book

#Create your ModelForm Here
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

        #Applying labels on Model Fields
        labels={
            'srno':'Sr No',
            "bookname":"Book Name",
            'author':'Author Name',
            'isbn':'ISBN NO',
            'category':'Category'
        }

        #Applying widgets on Model Fields
        widgets={
            'srno':forms.NumberInput(
                attrs={
                    'placeholder':'e.g:101'
                }
            ),
            'bookname':forms.TextInput(
                attrs={
                    'placeholder':'Python'
                }
            ),
            'isbn':forms.NumberInput(
                attrs={
                'placeholder':'10001'
                }
            ),
            'category':forms.TextInput(
                attrs={
                    'placeholder':'e.g:Programming'
                }
            )
        }

 
 