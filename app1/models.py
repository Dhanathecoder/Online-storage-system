from django.db import models
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class File(models.Model):
    caption = models.CharField(max_length=100)
    file = models.FileField(upload_to="files/%y")
    file_name = models.CharField(max_length=255)
    file_file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def file_url(self):
        if self.file:
            return self.file.url
        elif self.file_file:
            return self.file_file.url
        else:
            return None

    def file_display(self):
        if self.file:
            file_url = self.file.url
            file_name = self.file.name.split('/')[-1]
        elif self.file_file:
            file_url = self.file_file.url
            file_name = self.file_file.name.split('/')[-1]
        else:
            return None
        return mark_safe(f'<a href="{file_url}" target="_blank">{file_name}</a>')
