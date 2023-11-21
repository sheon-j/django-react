from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

# 어드민 등록 방법 1
'''
admin.site.register(Post)
'''
# 어드민 등록 방법 2
'''
class PostAdmin(admin.ModelAdmin):
  pass

admin.site.register(Post, PostAdmin)
'''
# 어드민 등록 방법 3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  # 모델 리스트에 출력할 컬럼 지정
  list_display = [
    'pk', # 'id' == 'pk' (alias),
    'image',
    'message', 'message_length', 
    'shorten_message', 'is_public',
    'created_at', 'updated_at',
  ]
  list_display_links = ['message'] # 진입 링크 설정
  list_filter = ['created_at', 'is_public'] # 지정 필드값으로 필터링 옵션
  search_fields = ['message'] # admin 페이지에서 쿼리


  # 커스텀 멤버를 어드민 단에서 구현하는 방법
  def shorten_message(self, post):
    return post.message[:3]
  
  def image(self, post):
    if post.photo:
      # 안전하다는 인증
      return mark_safe(f'<img src="{post.photo.url}" style="width: 68px">')