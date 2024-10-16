import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from travel.models import Country


#На основе модели
class CountrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # для предзаполненого поля user post request

    class Meta:
        model = Country
        fields = '__all__'

# #Сериализатор для преобразование обьекта в JSON на основе определенной модели
# class CountrySerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     con_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Country.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):(instance ссылка на обьект модели)
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.con_id = validated_data.get('con_id', instance.con_id)
#         instance.save()
#         return instance
#
#
# # """Детально как работает сериализатор(преоброзование обьекта в JSON)"""
# #
#
# class CountryModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# class CountrySerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
#
# def encode():
#     model = CountryModel('title', 'content')
#     model_sr = CountrySerializer(model)
#     json = JSONRenderer().render(model_sr.data)
#     return json
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "title", "content": "content"}')
#     data = JSONParser().parse(stream)
#     serializer = CountrySerializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     return serializer.validated_data
