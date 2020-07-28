from django.urls import path

from .Login.Controller import *

urlpatterns = [
    #AUTENTICA USUARIO
    path('Login', Login.login),
    path('', Login.login),
    path('Home', Login.login),
    path('EsqueciMinhaSenha', Login.esqueci_minha_senha),
    path('AlteraSenha/<slug:token>', Login.altera_senha),
    path('Deslogar', Login.deslogar),
    # path('BuscaTipoCliente', Login.busca_tipo_cliente),
    # path('AlteraEmpresaLogada', Login.loga_outra_empresa_grupo),
    # path('GeraTokenAlterarSenha', Login.gera_chave_alterar_senha),
    # path('BuscaGraficosHome', Login.graficos_home),
]