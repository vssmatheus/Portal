from ....conexao import Conexao
import json

class LoginDao:
    def realiza_login(self, param):
        cx = Conexao()
        cx.conectar()
        sql = """ SELECT CODIGO,
                         NOME,
                         EMAIL,
                         SENHA,
                         LOGIN,
                         DATA_CADASTRO,
                         CASE STATUS_USUARIO
                            WHEN  'A' then 'ATIVO'
                            WHEN  'B' then 'BLOQUEADO'
                            WHEN  'C' then 'CANCELADO'
                         END AS DESCRICAO_STATUS
                  FROM AG_USUARIO_PORTAL
                  WHERE UPPER(STATUS_USUARIO) = 'A'
                  AND LOGIN = %(Login)s
                  AND SENHA = %(Senha)s
             """
        resul = []
        resul = cx.select(sql, param)

        msg = ''

        if 'RowsEffect' in resul:
            if int(resul['RowsEffect']) > 0:
                msg = {'Mensagem': 'Bem vindo!', 'Tipo': 'success'}
        else:
            msg = {'Mensagem': 'Login ou Senha invalida!', 'Tipo': 'error'}

        return msg
