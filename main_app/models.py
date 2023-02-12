from django.db import models

# Create your models here.
STATUS=(
    ('N','Not Started'),
    ('S','Started'),
    ('C','Completed'),
    ('A','Abandoned'),
)

RATING=(
    (1, '1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5')
)

TYPE = (
    ("B","Book"),
    ("P", "Podcast"),
    ("M","Movie"),
    ("A", "Article"),
    ("V", "Video"),
    ("P", "Paper")
)

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Media(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField(
        choices=RATING,
        )
    type = models.CharField(
        max_length=100,
        choices=TYPE,
        default=TYPE[0][0]
        )
    authors = models.ManyToManyField(Author)
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )

    notes = models.TextField(max_length=1000)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"




