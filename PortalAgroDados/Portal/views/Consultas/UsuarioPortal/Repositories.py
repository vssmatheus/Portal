from ...Funcoes.Controller import Funcoes
from ....conexao import Conexao
import requests
from django.conf import settings
import json

class ConsultarUsuarioPortalDao:
    def consultar_usuario_portal(self, param):
        cx = Conexao()
        cx.conectar()

        sql = """
                SELECT USU.CODIGO,
                       USU.NOME,
                       USU.EMAIL,
                       USU.SENHA,
                       USU.LOGIN,
                       USU.DATA_CADASTRO,
                       CASE USU.STATUS_USUARIO
                            WHEN  'A'  THEN 'ATIVO'
                            WHEN  'B' THEN 'BLOQUEADO'
                            WHEN  'C' THEN 'CANCELADO'
                       END AS DESCRICAO_STATUS,
                       PER.PERM_ALTERACAO ALTERAR,
                       PER.PERM_EXCLUSAO EXCLUIR,
                       PER.PERM_IMPRESSAO IMPRIMIR,
                       PER.PERM_INCLUIR INCLUIR,
                       PER.PERM_VISUALIZAR_LOGIN VISUALIZAR_LOGINS
                FROM AG_USUARIO_PORTAL USU,
                     AG_PERMISSOES PER
                WHERE USU.CODIGO = PER.CODIGO
        """
        if 'LoginUsuario' in param:
            if param['LoginUsuario'] != '':
                param['LoginUsuario'] = '%{}%'.format(param['LoginUsuario'])
                sql += """ AND UPPER(TRIM(USU.LOGIN)) LIKE UPPER(TRIM(%(LoginUsuario)s ))"""

        if 'NomeUsuario' in param:
            if param['NomeUsuario'] != '':
                param['NomeUsuario'] = '%{}%'.format(param['NomeUsuario'])
                sql += """ AND UPPER(TRIM(USU.NOME)) LIKE UPPER(TRIM(%(NomeUsuario)s ))"""

        if 'StatusUsuario' in param:
            if param['StatusUsuario'] != '' and param['StatusUsuario'] != 'TD':
                sql += """ AND USU.STATUS_USUARIO =:StatusUsuario """

        sql += """ ORDER BY LOGIN """


        resul = cx.select(sql, param)

        return resul