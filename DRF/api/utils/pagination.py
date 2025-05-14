import math
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination
# from rest_framework.settings import api_settings
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    max_page_size = 1000
    
    def get_paginated_response(self, data):
        page_size = self.get_page_size(self.request)
        if not page_size:
            page_size = api_settings.PAGE_SIZE
            
        return Response({
            'links': {
                'next':self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'limit': self.get_previous_link(),
            'pages': math.ceil(self.page.paginator.count / page_size),
            'result': data    
        })