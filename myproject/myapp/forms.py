


from  django.forms import ModelForm ,TextInput ,DateInput, Textarea
from  myapp.models import Video
import datetime

class VideoForm(ModelForm):
    class Meta:
        model = Video
        today = datetime.date.today()
        fields = ["id",'title', 'published_date', 'short_details']
        widgets = {
            'title': TextInput(attrs={"size":30  , 'class': 'form-control'}),
            'published_date': DateInput(attrs={"format": "%Y-%m-%d", 'class': 'form-control' ,'value':today }),
            'short_details': TextInput(attrs={'class': 'form-control'}),
        }