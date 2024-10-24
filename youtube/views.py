from django.shortcuts import render, redirect
from .forms import VideoAnalysisForm
from .models import YouTubeVideo
from django.conf import settings
import requests, re


def extract_video_id(url):
    youtube_regex = (r'(https?://)?(www\.)'
                     '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                     '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    
    match = re.match(youtube_regex, url)
    return match.group(6) if match else None

