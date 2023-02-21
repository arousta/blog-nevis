from rest_framework.generics import RetrieveAPIView

from .models import Post
from .serializers import PostSerializer


class PostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    template_name = "post/post.html"
