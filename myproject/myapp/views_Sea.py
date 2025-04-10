from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Video
from django.views import View

# Create your views here.
# def hello_django(request):
#     return HttpResponse  ("Hellow django")

def hello_django(request):
    return render (request ,'hello.html' )

def show_video(request):
    if request.method == "GET":
        video = Video.objects.all()
        return render (request ,"listvideo.html" , {"videolist":video})
    






# class show_video_class(View):
class show_form(View):
    def get(self, request):
        form = VideoForm()
        return render(request, "videoform.html" , {'form': form})  
    

    def post(self, request):
        form = VideoForm(request.POST)
        if form.is_valid():
            v = Video(title = form.cleaned_data['title'],
                       description = form.cleaned_data['description'],
                       short_details = form.cleaned_data['short_details'])
            v.save()
            return HttpResponse("Video saved successfully!")
        else:
            return render(request, "thank.html")
