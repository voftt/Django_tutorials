from django.db import models

class Project(models.Model):
    title = models.CharField('타이틀', max_length=200)
    description = models.TextField('프로젝트 내용')
    tech = models.CharField('사용기술', max_length=100)
    image = models.ImageField('프로젝트 이미지', blank=True, null=True, upload_to='project')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
