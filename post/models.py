from django.db import models
from account.models import User
from datetime import datetime
from core.models import TimestampModel

#Post Model
class Post(TimestampModel):
    content = models.TextField(blank=True, verbose_name="방명록 내용")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    class Meta:
        db_table = "post"
        verbose_name= "방명록"
        ordering=["-created_at"]

class PostImage(TimestampModel):
    post_id = models.ForeignKey(Post, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', blank=True, null=True)

    class Meta:
        db_table = "postImage"
        ordering=["created_at"]

# Comment Model
class Comment(TimestampModel):
    content = models.TextField(blank=True, verbose_name="댓글 내용")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)


# #Like Model
# class Like(models.Model):


# class Report(models.Model):