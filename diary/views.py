from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from .permissions import IsAuthorOrReadonly, IsAuthor


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    # 게시글 목록 READ
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글 CREATE
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailView(APIView):
    """
    Custom Permission 클래스를 적용하기 위해, FBV를 CBV로 수정함.
    """
    permission_classes = [IsAuthorOrReadonly]

    def get_object(self, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        self.check_object_permissions(self.request, article)
        return article

    # 게시글 상세 페이지 READ
    def get(self, request, article_pk):
        article = self.get_object(article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 UPDATE
    def put(self, request, article_pk):
        article = self.get_object(article_pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    # 게시글 DELETE
    def delete(self, request, article_pk):
        article = self.get_object(article_pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # 댓글 목록 READ
    if request.method == 'GET':
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # 댓글 CREATE
    else:
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailView(APIView):
    permission_classes = [IsAuthor]

    def get_object(self, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        self.check_object_permissions(self.request, comment)
        return comment

    # 댓글 UPDATE
    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    # 댓글 DELETE
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)