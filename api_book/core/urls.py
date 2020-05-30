from rest_framework.routers import DefaultRouter
from .views import Book_ViewSet

router = DefaultRouter()
router.register('', Book_ViewSet, basename='books')

book_url = router.urls

