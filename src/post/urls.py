from django.urls import path, include
from post import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('nuevo', views.NuevoUser.as_view(), name='nuevousuario'),
    path('<slug>/', views.PostDetail.as_view(), name='detail'),
    path('create', views.CreatePost.as_view(), name='createpost'),
    path('update/<int:pk>', views.UpdatePost.as_view(), name='updatepost'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='deletepost'),
    path('like/<slug>', views.LikeView.as_view(), name='like'),
    path('sobremi', views.sobre_mi.as_view(), name='sobremi')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)