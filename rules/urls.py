from django.conf.urls import url, patterns
from rules.views import *

urlpatterns = patterns(
    '',
    url(
        r'^rules/upload/$',
        UploadRules.as_view(),
        name='upload_rules'
    ),
    url(
        r'^rules/upload-success/$',
        UploadSuccess.as_view(),
        name='upload_success'
    ),
)
