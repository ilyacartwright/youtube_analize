from django.shortcuts import render
from youtube.forms import VideoAnalysisForm

def main(request):
    form = VideoAnalysisForm()
    return render(request, 'index.html', {'form': form})
