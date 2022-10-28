from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleSerializer



# Create your views here.


# class 장점 : 상속이 가능하다.
class ArticleView(APIView):
    def get(self, request, format=None):
        if request.method == 'GET':
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
