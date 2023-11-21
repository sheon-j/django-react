from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# 주의: 사용자 settings를 합친 최종 settings를 import 해야함
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('instagram/', include('instagram.urls')),
]
if settings.DEBUG:
    # 프로덕션에서 미디어 파일을 운영하지 않음 (명시적인 setting.DEBUG 조건 추가)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) # 미디어 url 매핑