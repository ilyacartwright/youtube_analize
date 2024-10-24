from django.db import models
from accounts.models import CustomUser

class YouTubeVideo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video_url = models.URLField()
    video_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    publiched_at = models.DateTimeField()
    views_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class VideoAnalysis(models.Model):
    video = models.OneToOneField(YouTubeVideo, on_delete=models.CASCADE)
    seo_score = models.DecimalField(max_digits=5, decimal_places=2)
    title_keywords = models.TextField()
    description_keywords = models.TextField()
    sentiment_analysis = models.JSONField()
    visual_analysis = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.video.title


class Report(models.Model):
    video = models.ForeignKey(YouTubeVideo, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='reports/')
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.video.title
    
class Comment(models.Model):
    video = models.ForeignKey(YouTubeVideo, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    sentiment = models.CharField(max_length=10)
    published_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.video.title