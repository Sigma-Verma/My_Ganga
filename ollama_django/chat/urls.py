from django.urls import path
from .views import chat_page , chat_with_llm

urlpatterns = [
    path('', chat_page, name='chat_page'),
    path('query/', chat_with_llm, name='chat_with_llm'),
]
