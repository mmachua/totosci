from django import forms
from document.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('user','name','description', 'document',
                  'type','urgency','specification'
                  )