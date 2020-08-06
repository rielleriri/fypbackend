"""myfyp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from werespond import views

router = DefaultRouter()
router.register(r'users', views.UserListViewSet)
router.register(r'posts', views.PostListViewSet)
router.register(r'comments', views.CommentListViewSet)
router.register(r'reports', views.ReportListViewSet)
router.register(r'saves', views.SaveListViewSet)
router.register(r'votes', views.VoteListViewSet)
router.register(r'groups', views.GroupListViewSet)
router.register(r'cases', views.CaseListViewSet)
router.register(r'events', views.EventListViewSet)
router.register(r'events/(?P<users>[0-9]+)', views.EventListViewSet, basename='events_not_joined')
router.register(r'achievements', views.AchievementListViewSet)
router.register(r'achievement_rewards', views.AchievementRewardListViewSet)
router.register(r'certificates', views.CertificateListViewSet)
router.register(r'awarded_certificates', views.AwardedCertificateListViewSet)
# router.register(r'post', views.PostViewSet)
# router.register(r'save', views.SaveViewSet)
# router.register(r'vote', views.VoteViewSet)
# router.register(r'group', views.GroupViewSet)
# router.register(r'case', views.CaseViewSet)
# router.register(r'achievement', views.AchievementViewSet)
# router.register(r'user_achievement', views.UserAchievementViewSet)
# router.register(r'achievement_reward', views.AchievementRewardViewSet)
# router.register(r'report', views.ReportViewSet)
# router.register(r'user_certificate', views.UserCertificateViewSet)
# router.register(r'certificate', views.CertificateFormViewSet)
# router.register(r'event', views.EventViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)