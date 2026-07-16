from rest_framework.views import APIView
from rest_framework.response import Response

# View for the api/books

class BookView(APIView):
 
    def get(self, request, *args, **kwargs):
        return Response({"hello": "Django"})
    

book_view = BookView.as_view()
