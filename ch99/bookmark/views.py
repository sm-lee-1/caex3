from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView

class BookmarkLV(ListView):    # 테이블의 레코드 리스트를 보여주기 위한 뷰
    model = Bookmark

class BookmarkDV(DetailView):  # 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰
    model = Bookmark
