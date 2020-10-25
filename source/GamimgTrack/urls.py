from django.urls import path
from GamimgTrack import views_user, views_postagens, views

urlpatterns = [
    path('register/', views_user.RegisterUser), 
    path('info/', views_user.mostrar_detalhes),
    path('', views_user.LoginUser), 
    path('changeMyPass/', views_user.AlterarSenhaUser), 
    path('changeMyName/', views_user.AlterarLoginUser), 
    path('changeMyEmail/', views_user.AlterarNomeUser), 
    path('deleteMyUser/', views_user.DeletarMinhaConta), 
    path('listarUsers/', views_user.ListarUsuarios),
    path('listarPostagens/', views_postagens.listar_postagens),
    path('apagarConta/', views_user.ApagarOutraConta),
    path('meusPosts/', views_user.mostrar_meus_posts),

    path('criarNovaPostagem/', views_postagens.criar_nova_postagem),
]
