from django.urls import path 
from .views import *
urlpatterns = [
    path('cadastro', cadastro, nome='cadastro'),
    path('login', login, nome='login'),
    path('dashboard', dashboard, nome='dashboard'),
    path('logout', logout, nome='logout'),
    path('cria-prato', cria_prato, nome='cria_prato'),
    path('deleta/<int:prato_id>', deleta_prato, nome='deleta_prato'),
    path('edita/<int:prato_id>', edita_prato, nome='edita_prato'),
    path('atualiza_prato', atualiza_prato, nome='atualiza_prato'),
]
