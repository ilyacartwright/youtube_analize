from django import forms

class VideoAnalysisForm(forms.Form):
    video_url = forms.URLField(label='YouTube video URL', max_length=200, required=True)