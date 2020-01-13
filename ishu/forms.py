from django import forms
from .models import Product

class Product_Form(forms.ModelForm):
    title = forms.CharField(label='DISEASE',widget=forms.TextInput(attrs={"placeholder":"Disease"}))
    locality = forms.CharField(label='LOCALITY',widget=forms.TextInput(attrs={"placeholder":"Locality"}))
    class Meta:
        model = Product
        fields = [
            'title',
            'locality'
        ]  

    def clean_title(self):
        title = self.cleaned_data.get("title")
        title = title.lower()
        l = ['aids','malaria','dengue','loose motions']
        if title in l:
            return title
        else:
            raise forms.ValidationError("Not a valid disease")
        
    def clean_local(self):
        locality = self.cleaned_data.get("locality")
        locality = locality.lower()
        l = ['kharghar','andheri','thane','dadar']
        if locality in l:
            return locality
        else:
            raise forms.ValidationError("Not a valid locality")


# class Mun_Form(forms.ModelForm):
#     locality = forms.CharField(label='LOCALITY',widget=forms.TextInput(attrs={"placeholder":"Locality"}))
#     class Meta:
#         fields = [
#             'locality'
#         ]  
        
#     def clean_local(self):
#         local = self.cleaned_data.get("locality")
#         local = title.lower()
#         l = ['kharghar','andheri','thane','dadar']
#         if local in l:
#             return local
#         else:
#             raise forms.ValidationError("Not a valid locality")
