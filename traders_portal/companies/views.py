from rest_framework import generics, status
from rest_framework.response import Response

from .pagination import CustomPagination
from .models import Company, Watchlist
from .serializers import CompanySerializer, WatchlistSerializer


class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanySearchView(generics.ListAPIView):
    serializer_class = CompanySerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Company.objects.all()
        company_name = self.request.query_params.get('company_name', None)
        if company_name:
            queryset = queryset.filter(company_name__icontains=company_name)
        return queryset


class AddToWatchlistView(generics.CreateAPIView):
    

    def post(self, request):
        user = request.user
        company_id = request.data.get('company_id')
        try:
            company = Company.objects.get(id=company_id)
            watchlist, created = Watchlist.objects.get_or_create(
                user=user, company=company)
            if created:
                return Response({'status': 'Company added to watchlist'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'Company already in watchlist'}, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
class UserWatchlist(generics.ListAPIView):
    serializer_class = WatchlistSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)
