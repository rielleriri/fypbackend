from .models import Profile, Report, Case, Group, Post, PostSave, PostVote, Comment, AchievementReward, Achievement, Event, Certificate, AwardedCertificate
from .serializers import GroupSerializer, CaseSerializer, EventSerializer, CertificateSerializer, AwardedCertificateSerializer, CommentSerializer, PostSaveSerializer, PostVoteSerializer, PostSerializer, ReportSerializer, AchievementRewardSerializer, AchievementSerializer, ProfileSerializer
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser, MultiPartParser

class UserListViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ReportListViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    # if request.method == 'POST':
    #     serializer = ReportSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     else:
    #         return Response(serializer.errors, status=400)

class PostListViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    parser_classes = (MultiPartParser, JSONParser)

class CommentListViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

class ReportListViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    parser_classes = (MultiPartParser, JSONParser)

class SaveListViewSet(viewsets.ModelViewSet):
    queryset=PostSave.objects.all()
    serializer_class=PostSaveSerializer

class VoteListViewSet(viewsets.ModelViewSet):
    queryset=PostVote.objects.all()
    serializer_class=PostVoteSerializer

class GroupListViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer
    parser_classes = (MultiPartParser, JSONParser)

class CaseListViewSet(viewsets.ModelViewSet):
    queryset=Case.objects.all()
    serializer_class=CaseSerializer

class EventListViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    parser_classes = (MultiPartParser, JSONParser)

class AchievementListViewSet(viewsets.ModelViewSet):
    queryset=Achievement.objects.all()
    serializer_class=AchievementSerializer

class AchievementRewardListViewSet(viewsets.ModelViewSet):
    queryset=AchievementReward.objects.all()
    serializer_class=AchievementRewardSerializer
    parser_classes = (MultiPartParser, JSONParser)

class CertificateListViewSet(viewsets.ModelViewSet):
    queryset=Certificate.objects.all()
    serializer_class=CertificateSerializer
    parser_classes = (MultiPartParser, JSONParser)

class AwardedCertificateListViewSet(viewsets.ModelViewSet):
    queryset=AwardedCertificate.objects.all()
    serializer_class=AwardedCertificateSerializer

