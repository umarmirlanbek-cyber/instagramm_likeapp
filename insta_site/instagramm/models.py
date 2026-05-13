from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    user_image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user_network = models.URLField(null=True, blank=True)
    certificate = models.BooleanField(default=False)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

    def get_count_followers(self):
        return self.followers.count()


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.follower} {self.following}'


class Post(models.Model):
    music = models.FileField()

    def __str__(self):
        return str(self.music)


class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='contents')
    file = models.FileField()

    def __str__(self):
        return str(self.id)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_likes')
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user} {self.post}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.post}'


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comment_likes')
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.comment}'


class SavePost(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='save_post')

    def __str__(self):
        return self.user.username


class SavePostItem(models.Model):
    save_post = models.ForeignKey(SavePost, on_delete=models.CASCADE, related_name='items')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saved_items')

    def __str__(self):
        return f'{self.save_post} {self.post}'


class Storia(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='storias')
    file = models.FileField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
