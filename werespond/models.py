from __future__ import unicode_literals
from django.db import models
import datetime as dt

# Create your models here.

class Profile(models.Model):
    profile_hp = models.IntegerField(unique=True, primary_key=True)
    profile_name = models.CharField(max_length=60)
    GENDER_TYPES =(
        ('m', 'Male'),
        ('f', 'Female'),
    )
    profile_gender = models.CharField(max_length=1, choices=GENDER_TYPES, default='m')
    is_scdf = models.BooleanField(default=False)
    profile_email = models.EmailField(max_length=254)
    profile_created_at= models.DateTimeField("User Created At", auto_now_add=True, editable=True)

    def get_username(self):
        return self.user.username

class Report(models.Model):
    #id primary key auto added if not specified
    report_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='reports') #one-to-many rs
    report_location = models.CharField(max_length=250)
    report_description = models.CharField(max_length=250)
    report_image = models.ImageField(upload_to=None, blank=True)
    report_date = models.DateTimeField(auto_now_add=True, editable=True)

    REPORT_TYPES = (
        ('c', 'Cardiac Arrest'),
        ('f', 'Fire Report'),
        ('h', 'Fire Hazard')
    )

    report_type = models.CharField(
        max_length=1,
        choices = REPORT_TYPES,
    )

class Case(models.Model):
    location = models.CharField(max_length=600)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateField(auto_now_add=True, editable=True)
    description = models.CharField(max_length=600)
    updated_at = models.DateTimeField(auto_now=True, editable=True) #default setting editable=False, blank=True
    #many-to-many rs
    users = models.ManyToManyField(Profile, related_name='cases', blank=True)

    CASE_TYPES = (
        ('c', 'Cardiac Arrest'),
        ('f', 'Fire Case'),
    )

    case_type = models.CharField(
        "Case Type",
        max_length=1,
        choices=CASE_TYPES,
    )
# a case can be shown to many users 

class Group(models.Model):
    profile_pic = models.ImageField(upload_to=None, null=True)
    display_pic = models.ImageField(upload_to=None, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    email = models.EmailField(max_length=254, blank=True, null=True)
    website = models.CharField(max_length=155)
    members = models.ManyToManyField(Profile, related_name='groups', blank=True)
    created_at= models.DateTimeField(auto_now_add=True, editable=True)
    #updated_at = models.DateTimeField(auto_now=True, editable=True) #default setting editable=False, blank=True

class Post(models.Model):
    post_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts", null=True)
    post_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name="posts_in_group")
    post_body = models.CharField(max_length=1000)
    post_image = models.ImageField(upload_to=None, null=True, blank=True)
    post_date= models.DateTimeField(auto_now_add=True, editable=True)
    #updated_at = models.DateTimeField("Updated At", auto_now=True, editable=True) #default setting editable=False, blank=True

class PostSave(models.Model):
    save_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="saves", null=True)
    save_post = models.ForeignKey(Post, related_name='user_who_saved', on_delete=models.CASCADE, null=True)

class PostVote(models.Model):
    vote_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="votes", null=True)
    vote_post = models.ForeignKey(Post, related_name='user_who_voted', on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, related_name='user_who_commented', on_delete=models.CASCADE, null=True)
    comment_user = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE, null=True)
    comment_content = models.CharField(max_length=300)
    comment_date= models.DateTimeField(auto_now_add=True, editable=True)

class Achievement(models.Model):
    achv_name = models.CharField(max_length=50)
    achv_condition = models.CharField(max_length=50)
    achv_created_at = models.DateTimeField(auto_now_add=True, editable=True)
    achv_users = models.ManyToManyField(Profile, related_name='achievements', blank=True)

class AchievementReward(models.Model):
    rew_achievement = models.OneToOneField(Achievement, on_delete=models.CASCADE, primary_key=True)
    rew_reward = models.ImageField(upload_to=None, null=True)

class Event(models.Model):
    slots = models.IntegerField()
    image = models.ImageField(upload_to=None, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField( max_length=500)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    users = models.ManyToManyField(Profile, related_name='events', blank=True)   

class Certificate(models.Model):
    cert_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certificates', null=True)
    CERT_TYPES = (
        ('c', 'CPR'),
        ('a', 'AED'),
        ('b', 'CPR+AED'),
        ('s', 'Standard First Aid'),
        ('o', 'Occupational First Aid'),
        ('p', 'Psychological First Aid'),
        ('f', 'Fire Safety')
    )
    cert_cert_type = models.CharField(
        max_length=1,
        choices=CERT_TYPES,
    )
    cert_image = models.ImageField(upload_to=None, null=True)
    cert_expiry = models.DateField()

class AwardedCertificate(models.Model):
    CERT_OPTIONS = (
        ('c', 'CPR'),
        ('a', 'AED'),
        ('b', 'CPR+AED'),
        ('s', 'Standard First Aid'),
        ('o', 'Occupational First Aid'),
        ('p', 'Psychological First Aid'),
        ('f', 'Fire Safety')
    )
    awcert_cert_type = models.CharField(
        "User Cert Type",
        max_length=1,
        choices=CERT_OPTIONS,
    )
    awcert_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='awarded', null=True)
    awcert_expiry = models.DateField()
    awcert_awarded_at = models.DateTimeField(auto_now_add=True, editable=True)

# class QuizQuestion(models.Model):
#     id = models.AutoField(primary_key=True)
#     question = models.CharField("Quiz Qns", max_length=400)

#     class Meta:
#         ordering = ('id',)

# class QuizChoice(models.Model):
#     id = models.AutoField(primary_key=True)
#     is_correct = models.BooleanField("Correct Ans")
#     question = models.ForeignKey('QuizQuestion', on_delete=models.CASCADE)
#     choice = models.CharField("Choice", max_length=500)

#     class Meta:
#         ordering = ('id',)

# class QuizUserAnswer(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey('Profile', on_delete=models.CASCADE)
#     question = models.ForeignKey('QuizQuestion', on_delete=models.CASCADE)
#     question_choice = models.ForeignKey('QuizChoice', on_delete=models.CASCADE)
#     point_awarded = models.BooleanField

#     class Meta:
#         ordering = ('id',)
