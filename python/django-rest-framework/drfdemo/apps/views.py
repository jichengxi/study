from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from apps.models import Book
from apps.ser import BookSerializer, BookModelSerializer
from rest_framework.response import Response
from apps.utils import MyResponse
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action  # 装饰器
from apps import models
import uuid
from apps.apps_auth import MyAuthentication


class BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(nid=pk).first()
        # 用BookSerializer类去实例化一个对象，序列化谁就传过来谁
        book_ser = BookSerializer(book)
        # book_ser.data 序列化对象.data就是序列化之后的字典
        return Response(book_ser.data)

    def put(self, request, pk):
        response_msg = MyResponse()
        # 先取到这个对象
        book = Book.objects.filter(nid=pk).first()
        # 得到一个序列化的类对象
        # print(book)
        # print(request.data)
        book_ser = BookSerializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg.data = book_ser.data
        else:
            response_msg.status = '101'
            response_msg.msg = '数据校验未通过'
            response_msg.data = book_ser.errors
        return Response(response_msg.get_dict)

    def delete(self, request, pk):
        Book.objects.filter(pk=pk).delete()
        response_msg = MyResponse()
        return Response(response_msg.get_dict)


class BooksView(APIView):
    def get(self, request):
        response_msg = MyResponse()
        books = Book.objects.all()
        books_ser = BookSerializer(books, many=True)
        response_msg.data = books_ser.data
        return Response(response_msg.get_dict)

    # 新增
    def post(self, request):
        response_msg = MyResponse()
        book_ser = BookSerializer(data=request.data)
        # 校验字段
        if book_ser.is_valid():
            book_ser.save()
            response_msg.data = book_ser.data
        else:
            response_msg.status = '101'
            response_msg.msg = '数据校验未通过'
            response_msg.data = book_ser.errors
        return Response(response_msg.get_dict)


class BooksModelView(APIView):
    def get(self, request):
        response_msg = MyResponse()
        books = Book.objects.all()
        books_ser = BookModelSerializer(books, many=True)
        response_msg.data = books_ser.data
        return Response(response_msg.get_dict)


class BooksView2(GenericAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer

    def get(self, request):
        response_msg = MyResponse()
        books = self.get_queryset()
        books_ser = self.get_serializer(books, many=True)
        response_msg.data = books_ser.data
        return Response(response_msg.get_dict)

    # 新增
    def post(self, request):
        response_msg = MyResponse()
        book_ser = self.get_serializer(data=request.data)
        # 校验字段
        if book_ser.is_valid():
            book_ser.save()
            response_msg.data = book_ser.data
        else:
            response_msg.status = '101'
            response_msg.msg = '数据校验未通过'
            response_msg.data = book_ser.errors
        return Response(response_msg.get_dict)


class BookView2(GenericAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer

    def get(self, request, pk):
        book = self.get_object()
        book_ser = self.get_serializer(instance=book)
        return Response(book_ser.data)

    def put(self, request, pk):
        response_msg = MyResponse()
        book = self.get_object()
        book_ser = self.get_serializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg.data = book_ser.data
        else:
            response_msg.status = '101'
            response_msg.msg = '数据校验未通过'
            response_msg.data = book_ser.errors
        return Response(response_msg.get_dict)

    def delete(self, request, pk):
        self.get_object().delete()
        response_msg = MyResponse()
        return Response(response_msg.get_dict)


class BooksView3(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookView3(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book.objects
    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class BooksView4(ListCreateAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer


class BookView4(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer


class BookView5(ModelViewSet):
    queryset = Book.objects
    serializer_class = BookSerializer


class BookView6(ReadOnlyModelViewSet):
    queryset = Book.objects
    serializer_class = BookSerializer


class BookView7(ModelViewSet):
    authentication_classes = [MyAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # 在默认的路由路径外，自定义的路由路径
    # action是装饰器. methods是一个列表，放请求方式. detail
    @action(methods=['get', 'post'], detail=False)
    def get_1(self, request, pk):
        books = self.get_queryset()
        # print(books)
        print(request.user.username)
        # print(pk)
        ser = self.get_serializer(books, many=True)
        return Response(ser.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            # 登录成功, 生成一个随机字符串
            token = uuid.uuid4()
            # models.UserToken.objects.create(token=token, user=user) 每次登录都会创建一条记录
            # update_or_create 有就更新，没有就新增
            models.UserToken.objects.update_or_create(defaults={'token': token}, user=user)
            return Response({'status': 100, 'msg': '登录成功', 'token': token})
        else:
            return Response({'status': 101, 'msg': '用户名或密码错误'})
