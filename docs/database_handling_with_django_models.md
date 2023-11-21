- babel 코드 트랜스파일링: es6 이상의 코드를 범용적인 es5 문법으로 변환해줌

- 리액트 + 타입스크립트

- django.contrib 안에 장고 기본앱: admin, auth, messages, sessions, staticfiles

https://github.com/django/django/tree/master/django/contrib

- models 규칙 파스칼 네이밍, 단수형

---

- 설계한 데이터베이스 구조에 따라, 최대한 필드타입을 타이트하게 지정해주는 것이, 입력값 오류를 막을 수 있음.
  - 모델이 장고 개발의 절반
- django-admin-honeypot 앱을 통해 가짜 admin 페이지 노출하는 방법

---

### Static 파일

- 개발 리소스로서의 정적인 파일 (Js, css, image 등)
- 앱 / 프로젝트 단위로 저장 / 서빙

### Media 파일

- FileField/ImageField를 통해 저장한 모든 파일

- DB필드에는 저장경로를 저장하며, 파일은 파일 스토리지에 저장

  실제로 문자열을 저장하는 필드 (중요)

- 프로젝트 단위로 저장/서빙

### settings.MEDIA_URL/MEDIA_ROOT

- HttpRequest.FILES를 통해 파일이 전달
- 뷰 로직이나 폼 로직을 통해, 유효성 검증을 수행
- FileField / ImageField 필드에 '경로(문자열)'를 저장
- settings.MEDIA_ROOT 경로에 파일을 저장
- settings.MEDIA_URL 에 미디어 루트 경로에 매핑할 url 세팅

### FileField 와 ImageField

- FileField: File Storage API를 통해 파일을 저장

  - 장고에서는 File System Storage만 지원, django-storages를 통해 확장 지원
  - 해당 필드를 옵션 필드로 두고자 할 경우, blank=True 옵션 적용

- ImageField (FileField 상속)

  - Pillow를 통해 이미지 width/height 획득
  - 이미지가 포함된 레코드를 삭제하여도 media에 존재함 
    (배치성으로 참조여부를 필터링하여 삭제)
  - upload_to 파라미터: 미디어의 저장 공간을 트리구조로 분할하여 사용할 수 있음 (str|function)
    ex) `photo = models.ImageField(upload_to='blog/%Y/%m/%d')`
  - queryset.photo.url = media url 경로
    queryset.photo.path = media 절대 경로

- 커스텀 필드 (PDFField, ExcelField) 생성 가능

- File Upload Handler 디스크 풀 방지

  - 파일크기가 2.5MB 이하일 경우 메모리에 담겨 전달: MemoryFileUploadHandler
  - 파일크기가 2.5MB 초과일 경우 디스크에 담겨 전달: TemporaryFileUploadHandler
  - 관련 설정: settings.FILE_UPLOAD_MAX_MEMORY_SIZE

- 예시) uuid 를 통한 파일명 정하기

  ```python
  import os
  from uuid import uuid4
  from django.utils import timezone
  
  def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label			# 앱별
    cls_name = instance.__class__.__name__.lower()			# 클래스별
    ymd_path = timezone.now().strftime('%Y/%m/%d')			# 일자별
    uuid_name = uuid4().hex
    extension = os.path.splittext(filename)[-1].lower()	# 확장자 추출
    return '/'.join([
      app_label, cls_name, ymd_path, uuid_name[:2], uuid_name+extenmsion,
    ])
  ```

  



