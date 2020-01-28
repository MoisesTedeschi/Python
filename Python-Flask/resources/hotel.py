from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required
import sqlite3
from resources.filtros import normalize_path_parametros, consulta_sem_cidade, consulta_com_cidade


#Recenendo todos os parametros passados na busca
path_parametros = reqparse.RequestParser()
path_parametros.add_argument('cidade', type=str)
path_parametros.add_argument('estrelas_min', type=float)
path_parametros.add_argument('estrelas_max', type=float)
path_parametros.add_argument('diaria_min', type=float)
path_parametros.add_argument('diaria_max', type=float)
path_parametros.add_argument('limit', type=float)
path_parametros.add_argument('offset', type=float)


class Hoteis(Resource):
    #Listando todos os Hoteis.
    #def get(self):
    #   return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

    def get(self):
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()

        dados = path_parametros.parse_args()

        #Pagando os dados que não são nulos
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}

        #Retorna um json com os dados válidos
        parametros = normalize_path_parametros(**dados_validos)

        if not parametros.get('cidade'):
            #Recebendo Tupla de valores
            tupla = tuple([parametros[chaves] for chaves in parametros])
            resultado = cursor.execute(consulta_sem_cidade, tupla)

        else:
            # Recebendo Tupla de valores
            tupla = tuple([parametros[chaves] for chaves in parametros])
            resultado = cursor.execute(consulta_com_cidade, tupla)

        #Resultados que cumprem os critérios (um ou outro) entram na lista de hoteis.
        hoteis = []
        for linha in resultado:
            hoteis.append({
                'hotel_id': linha[0],
                'nome': linha[1],
                'estrelas': linha[2],
                'diaria': linha[3],
                'cidade': linha[4]
            })

        return {'hoteis': hoteis}
        #return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}



class Hotel(Resource):
    # Recebendo todos os elementos da requisição
    # Parser nos elementos JSON.
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="The field 'nome' cant be left blank.")
    argumentos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cant be left blank.")
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    #Pegando um Hotel via identificador.
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found!'}, 400

    @jwt_required
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400

        # Todos os elementos passados vão vir com Chave e Valor.
        dados = Hotel.argumentos.parse_args()

        # Criando um objeto do tipo hotelmodel, mas precisa ser convertido em lista para poder ser alterado.
        # Ou seja, um objeto não poderia ser adicionado na lista de hoteis.
        hotel_objeto = HotelModel(hotel_id, **dados)

        try:
            hotel_objeto.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel_objeto.json()

    @jwt_required
    def put(self, hotel_id):
        # Todos os elementos passados vão vir com Chave e Valor.
        dados = Hotel.argumentos.parse_args()

        # Adicionando novo hotel a lista.
        # Retornando novo Hotel adicionando.
        hotel_encontrado = HotelModel.find_hotel(hotel_id)

        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()

            return hotel_encontrado.json(), 200

        # Criando um objeto do tipo hotelmodel, mas precisa ser convertido em lista para poder ser alterado.
        # Ou seja, um objeto não poderia ser adicionado na lista de hoteis.
        hotel = HotelModel(hotel_id, **dados)

        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json(), 201

    @jwt_required
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)

        #Rerotna os hoteis - Para cada hotel > Se o hotel com ID em questão não for igual ao ID passado.
        #Ou seja, retorna uma nova lista sem o hotel com ID passado.
        #hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]

        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel.'}, 500

            return {'message': 'Hotel deleted!'}
        return {'message': 'Hotel not found.'}, 404