class Animal:
    def __init__(self, nome, especie, idade):
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_especie(self):
        return self.__especie

    def get_idade(self):
        return self.__idade

    def set_nome(self, nome):
        self.__nome = nome

    def set_especie(self, especie):
        self.__especie = especie

    def set_idade(self, idade):
        self.__idade = idade

    def fazer_som(self):
        return f"{self.__nome}, o {self.__especie}, fez um som!"

class Zoo:
    def __init__(self, nome, localizacao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__animais = []

    def get_nome(self):
        return self.__nome

    def get_localizacao(self):
        return self.__localizacao

    def get_animais(self):
        return self.__animais

    def set_nome(self, nome):
        self.__nome = nome

    def set_localizacao(self, localizacao):
        self.__localizacao = localizacao

    def adicionar_animal(self, animal):
        self.__animais.append(animal)

    def mostrar_animais(self):
        for animal in self.__animais:
            print(f"Nome: {animal.get_nome()}, Espécie: {animal.get_especie()}, Idade: {animal.get_idade()}")

if __name__ == "__main__":
    tigre = Animal("Rajah", "Tigre", 5)
    leao = Animal("Simba", "Leão", 7)
    elefante = Animal("Dumbo", "Elefante", 10)

    zoo = Zoo("Zoológico Central", "São Paulo")

    zoo.adicionar_animal(tigre)
    zoo.adicionar_animal(leao)
    zoo.adicionar_animal(elefante)

    zoo.mostrar_animais()

    print(tigre.fazer_som())
    print(leao.fazer_som())
    print(elefante.fazer_som())