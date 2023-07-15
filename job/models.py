from django.db import models
job_type=(
    ('part time','part time'),
    ('full tim ','full time'),
)
class Job (models.Model):
    title=models.CharField(max_length=10)
    #location
    job_type=models.CharField(max_length=15,choices=job_type)
    description=models.TextField(max_length=1000)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    published_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class category (models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name