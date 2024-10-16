from django.forms import model_to_dict
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from travel.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from travel.models import Country, Continent
from travel.serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['get', 'post'], detail=False) #декоратор для доп. url роутера для континентов
    def continent(self, request): # Список континентов
        con = Continent.objects.all()
        return Response({'con': [c.name for c in con]})

# class CountryApiView(generics.ListCreateAPIView): #(get,post)
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filter_fields = ['continent__name']
#     search_fields = ['title', 'user']
#
# class CountryUpdateView(generics.UpdateAPIView): (put, patch)
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
#     permission_classes = (IsAuthenticated, )
#
#
# class CountryDetailView(generics.RetrieveUpdateDestroyAPIView): (get,post,patch,delete)
#     queryset = Country.objects.all()(lazy query)
#     serializer_class = CountrySerializer
#     permission_classes = (IsOwnerOrReadOnly, )

# Base APIView
# class CountryApiView(APIView):
#     def get(self, request):
#         c = Country.objects.all()
#         return Response({'items': CountrySerializer(c, many=True).data})
#
#     def post(self, request):
#         serializer = CountrySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         #Нужен был пока в сериализаторе не было create
#         # post_new = Country.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     con_id=request.data['con_id'],
#         # )
#         #return Response({'item': CountrySerializer(post_new).data})
#
#         return Response({'item': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Country.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = CountrySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"items": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})
#         try:
#             Country.objects.filter(id=pk).delete()
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         return Response({'items': 'Delete item ' + str(pk)})
