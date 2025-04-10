from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Video
from django.views import View
from myapp.forms import VideoForm


# Create your views here.
# def hello_django(request):
#     return HttpResponse  ("Hellow django")

def hello_django(request):
    return render (request ,'hello.html' )

def show_video(request):
    if request.method == "GET":
        video = Video.objects.all()
        return render (request ,"listvideo.html" , {"videolist":video})
    
class show_video_class(View):
    def get(self, request):
        video = Video.objects.all()
        return render (request ,"listvideo.html" , {"videolist":video})
    






# class show_video_class(View):
class video_form(View):
    def get(self, request):
        form = VideoForm()
        return render(request, "videoform.html" , {'form': form})  
    
    def post(self, request):
        form = VideoForm(request.POST)
        if form.is_valid():
            v = Video(title = form.cleaned_data['title'],
                       published_date = form.cleaned_data['published_date'],
                       short_details = form.cleaned_data['short_details'])
            v.save()
            context = {'id': v.id, 'title': v.title, 'published_date' : v.published_date, 'short_details': v.short_details}
          
        return render(request, "thank.html" , context)
