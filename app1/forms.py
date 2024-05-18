from django import forms
from .models import File

from django import forms
from django.utils.safestring import mark_safe
from .models import File

class FileForm(forms.ModelForm):
    file = forms.FileField(label='Select a file', required=True, widget=forms.ClearableFileInput(attrs={'multiple': False}))

    class Meta:
        model = File
        fields = ('file',)

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        if self.instance.file:
            file_url = self.instance.file.url
            file_name = self.instance.file.name.split('/')[-1]
            file_html = f'<a href="{file_url}" target="_blank">{file_name}</a>'
            self.fields['file'].help_text = mark_safe(file_html)
