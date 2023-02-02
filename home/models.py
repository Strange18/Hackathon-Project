from django.db import models
from django.contrib.auth.models import User

municipality = [
    ('Kathmandu','Kathmandu'),
    ('Biratnagar','Biratnagar'),
    ('Pokhara','Pokhara'),
    ('Laltipur','Lalitpur'),
    ('Birgunj','Birgunj'),
    ('Bharatpur','Bharatpur')
]

# Create your models here.


class complain(models.Model):

    severe = [
        ('0', '0'),
        ('1', '1'),
        ('2','2'),
        ('3', '3'),
        ('4', '4'),
        ('5','5')
    ]
    department = [
        ('road', 'road'),
        ('water', 'water'),
        ('transportation', 'transportation'),
        ('education','education'),
        ('information technology','information technology'),
        ('finance','finance'),
        ('foreign affairs','foreign affairs'),
        ('agriculture','agriculture'),
        ('health','health'),

    ]
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    municipality = models.CharField(
        choices=municipality, null=False, blank=False, default='Kathmandu', max_length=50)
    severity = models.CharField(
        choices=severe, default=0, null=False, blank=False, max_length=50)
    department = models.CharField(
        choices=department, null=False, blank=False, default='road', max_length=50)
    date = models.DateField(auto_now_add=True)
    upvote = models.ManyToManyField(User,related_name='complain_likes',blank=True)
    downvote = models.ManyToManyField(User,related_name='complain_dislikes',blank=True)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.upvote.count()
    
    def total_dislikes(self):
        return self.downvote.count()


class idea(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    municipality = models.CharField(
        choices=municipality, null=False, blank=False, default='Kathmandu', max_length=50)
    upvote = models.ManyToManyField(User,related_name='idea_likes',blank=True)
    downvote = models.ManyToManyField(User,related_name='idea_dislikes',blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.upvote.count()
    
    def total_dislikes(self):
        return self.downvote.count()
