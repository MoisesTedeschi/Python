from flask_restful import Resource, reqparse
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST


#Pega os dados que o usuário passar.
atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cant be left blank.")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cant be left blank.")

class User(Resource):

    #Pegando um Hotel via identificador.
    # /usuarios/{user_id}
    def get(self, user_id):
        usuario = UserModel.find_user(user_id)
        if usuario:
            return usuario.json()
        return {'message': 'User not found!'}, 400

    @jwt_required
    def delete(self, user_id):
        usuario = UserModel.find_user(user_id)

        #Rerotna os hoteis - Para cada hotel > Se o hotel com ID em questão não for igual ao ID passado.
        #Ou seja, retorna uma nova lista sem o hotel com ID passado.
        #hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]

        if usuario:
            try:
                usuario.delete_user()
            except:
                return {'message': 'An error ocurred trying to delete user.'}, 500

            return {'message': 'User deleted!'}
        return {'message': 'User not found.'}, 404


class UserRegister(Resource):
    #/cadastro
    def post(self):
        # Variável dados recebe todos os dados do usuário.
        dados = atributos.parse_args()

        #Se o usuário já existe.
        if UserModel.find_by_login(dados['login']):
            return {"message": "The login '{}' already exists.".format(dados['login'])}

        user = UserModel(**dados)

        user.save_user()
        return {'message': 'User created successfully!'}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):

        #Variável dados recebe todos os dados do usuário.
        dados = atributos.parse_args()

        #Encontra o usuário pelo login.
        user = UserModel.find_by_login(dados['login'])
        #Se a senha passada pelo usuário for igual a senha registrada banco entra no bloco.
        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'access_token': token_de_acesso}, 200

        return {'message': 'The username or password is incorrect.'}, 401


#Classe Logout
class UserLogout(Resource):

    #Para fazer o logout o usuário precisa estar logado.
    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti'] #JWT Token Identifier
        BLACKLIST.add(jwt_id)

        return {'message': 'Logged out successfully!'}, 200