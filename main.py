import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def test_set_route(self):
        # Adicionar em S8
        print("função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        print("função criada para selecionar um plano")
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        print("função criada para preencher um número de telefone")
        pass

    def test_fill_card(self):
        # Adicionar em S8
        print("função criada para preencher um cartão")
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        print("função criada para fazer um comentário ao motorista")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        print("função criada para encomendar cobertor e lenço")
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            print("função criada para selecionar 2 sorvetes")
        pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        print("função criada para pesquisar modelo de carro")
        pass
