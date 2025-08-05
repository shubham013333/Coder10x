from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Post
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets 
from django.core.paginator import Paginator


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubscriptionSerializer
class PostListView(View):
    def get(self, request):
        # Order posts by published_date in descending order (latest first)
        posts = Post.objects.values('id', 'title', 'content', 'published_date').order_by('-published_date')
        
        paginator = Paginator(posts, 12)  # Show 10 posts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return JsonResponse(list(page_obj), safe=False)

class PostDetailView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'published_date': post.published_date,
        }
        return JsonResponse(data)


class SubscribeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subscription successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)