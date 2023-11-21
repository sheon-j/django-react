from django.db import models

class Post(models.Model):
  message = models.TextField()
  photo = models.ImageField(
    blank=True,
    # upload_to='instagram/post/%Y/%m/%d' # => media 파일이 많아지는 경우 분할하여 사용
  )
  is_public = models.BooleanField(default=False, verbose_name='공개여부')
  created_at = models.DateTimeField(auto_now_add=True) # 레코드가 생성될 때 입력
  updated_at = models.DateTimeField(auto_now=True) # 수정 시각이 입력
  '''
  python manage.py sqlmigrate instagram 0001_initial => sql 명령어 확인 가능
  BEGIN;
  --
  -- Create model Post
  --
  CREATE TABLE "instagram_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "message" text NOT NULL, "created_at" datetime NOT NULL, "update_at" datetime NOT NULL);
  COMMIT;

  python manange.py dbshell => sqlite로 진입
  sqlite> .tables => 테이블 목록 확인
  '''

  def __str__(self): # 객체의 string 화
    return f'[{self.id}] {self.message}' # <= orm 객체에서 대표되는 문자열
  
  def message_length(self): # 멤버 추가
    return len(self.message)
  
  '''
  # 이런 식으로 멤버 등록도 가능
  @property
  def username(self):
    return self.user.username
  '''
  
  # admin 페이지 컬럼명 변경
  message_length.short_description = '메세지 글자수'