from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views
from .views import PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',views.post_share,name = 'post_share'),
    path('<int:post_id>/comment/',views.post_comment,name = 'post_comment'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)