from django.db import models

class Episode(models.Model):
    """"EPISODE model
    Represents an episode from the rss feed source

    Attributes:
        title           the title of news topic
        description     the description of news topic
        pub_date        the date of publication of news topic
        link            the link to the original source of the news topic
        image           the image thumbnail for the news topic
        podcast_name    the name of the podcast
        guid            the unique id of the news topic
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"