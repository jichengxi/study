# from rest_framework.serializers import Serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.models import Book


class BookSerializer(serializers.Serializer):
    nid = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=10)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    author = serializers.CharField()
    publish = serializers.CharField()

    # 局部校验钩子
    def validate_price(self, data):
        # print(type(data))
        # print(data)
        if float(data) > 10:
            return data
        else:
            raise ValidationError('价格太低')

    # 全局校验钩子
    def validate(self, validated_data):
        # print(validated_data)
        author = validated_data.get('author')
        publish = validated_data.get('publish')
        if author == publish:
            raise ValidationError('作者名字和出版社名字一样')
        else:
            return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        instance.publish = validated_data.get('publish')
        instance.save()  # django orm提供的save()
        return instance

    def create(self, validated_data):
        # print(validated_data)
        instance = Book.objects.create(**validated_data)
        return instance


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['name', 'price']  # 指定序列化字段
        # exclude = ['publish']  # 和fields不能同时存在
        extra_kwargs = {
            'author': {'read_only': True}
        }
