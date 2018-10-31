from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field    = 'pk'

    serializer_class = BlogPostSerializer

    queryset        = BlogPost.objects.all()
