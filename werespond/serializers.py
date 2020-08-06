from rest_framework import serializers
import base64
from django.core.files.base import ContentFile
from .models import Profile, Report, Case, Group, Post, PostSave, PostVote, Comment, AchievementReward, Achievement, Event, Certificate, AwardedCertificate

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class GroupSerializer(serializers.ModelSerializer):
    grp_profile_pic = Base64ImageField(required=False)
    grp_display_pic = Base64ImageField(required=False)
    posts_in_group = serializers.SlugRelatedField(many=True, slug_field='post_group', queryset=Post.objects.all())
    class Meta:
        model = Group
        fields = ['id', 'grp_name', 'grp_profile_pic', 'grp_display_pic', 'grp_description', 'grp_email', 'grp_website', 'grp_created_at', 'grp_members', 'posts_in_group']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    event_image = Base64ImageField(required=False)
    class Meta:
        model = Event
        fields = ['id', 'event_name', 'event_description', 'event_image', 'event_date', 'event_time', 'event_venue', 'event_slots', 'event_users', 'event_created_at']

class CertificateSerializer(serializers.ModelSerializer):
    cert_image = Base64ImageField()
    class Meta:
        model = Certificate
        fields = ['cert_cert_type', 'cert_user', 'cert_image', 'cert_expiry']

class AwardedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardedCertificate
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSave
        fields = '__all__'

class PostVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVote
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    report_image=Base64ImageField()
    class Meta:
        model = Report
        fields = ['report_location', 'report_description', 'report_image', 'report_user', 'report_date']

    # def create(self, validated_data):
    #     report_image=validated_data.pop('report_image')
    #     report_location=validated_data.pop('report_location')
    #     report_description=validated_data.pop('report_description')
    #     report_date=validated_data.pop('report_date')
    #     report_user=validated_data.pop('report_user')
    #     return MyImageModel.objects.create(report_location=report_location, report_description=report_description, report_image=report_image, report_date=report_date)

class AchievementRewardSerializer(serializers.ModelSerializer):
    rew_reward = Base64ImageField()
    class Meta:
        model = AchievementReward
        fields = ['rew_achievement', 'rew_reward']

class AchievementSerializer(serializers.ModelSerializer):
    reward = AchievementRewardSerializer(read_only=True)
    class Meta:
        model = Achievement
        fields = ['achv_name', 'achv_condition', 'achv_created_at', 'reward', 'achv_users']

class ProfileSerializer(serializers.ModelSerializer):
    reports = serializers.SlugRelatedField(many=True, required=False, slug_field='report_description', queryset=Report.objects.all())
    cases = CaseSerializer(source='case_description', many=True, required=False)
    groups = GroupSerializer(source='grp_name', many=True, required=False)
    posts = serializers.SlugRelatedField(required=False, many=True, slug_field='post_body', queryset=Post.objects.all())
    saves = serializers.SlugRelatedField(required=False, many=True, slug_field='save_post', queryset=PostSave.objects.all())
    votes = serializers.SlugRelatedField(required=False, many=True, slug_field='vote_post', queryset=PostVote.objects.all())
    comments = serializers.SlugRelatedField(required=False, many=True, slug_field='comment_content', queryset=Comment.objects.all())
    achievements = AchievementSerializer(required=False, source='achv_name', many=True)
    events = EventSerializer(source='event_name', many=True, required=False)
    certificates = serializers.SlugRelatedField(required=False, many=True, slug_field='cert_cert_type', queryset=Certificate.objects.all())
    awarded = serializers.SlugRelatedField(required=False, many=True, slug_field='awcert_cert_type', queryset=AwardedCertificate.objects.all())
    class Meta:
        model = Profile
        fields = ['profile_hp', 'profile_name', 'profile_gender', 'is_scdf', 'profile_email', 'profile_created_at', 'reports', 'cases', 'groups', 'posts', 'saves', 'votes', 'comments', 'achievements', 'events', 'certificates', 'awarded']

class PostSerializer(serializers.ModelSerializer):
    post_image = Base64ImageField(max_length=None, use_url=True, required=False)
    user_who_saved = serializers.SlugRelatedField(required=False, many=True, slug_field='save_user', queryset=PostSave.objects.all())
    user_who_voted = serializers.SlugRelatedField(required=False, many=True, slug_field='vote_user', queryset=PostVote.objects.all())
    user_who_commented = CommentSerializer(read_only=True, many=True, required=False) # to list out all comments
    vote_count = serializers.IntegerField(source = 'user_who_voted.count', read_only=True, required=False)
    comment_count = serializers.IntegerField(source = 'user_who_commented.count', read_only=True, required=False)
    class Meta:
        model = Post
        fields = ['id', 'post_body', 'post_image', 'post_date', 'post_user', 'user_who_saved', 'user_who_voted', 'vote_count', 'user_who_commented', 'comment_count']

