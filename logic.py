from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.height = self.get_height()
        self.hp = randint(200, 250)
        self.power = randint(5, 10)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front-default'])
        else:
            return None
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['height'])
        else:
            return 0

    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name};\n Высота покеомона: {self.height};\n HP(Очки здоровья): {self.hp};\n PP(Очки силы): {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

class Fighter(Pokemon):
    def attack(self, enemy):
        superpower = randint(5,15)
        self.pp += superpower
        result = super().attack(enemy)
        self.pp -= superpower
        return result + f"\nБоец применил супер-атаку силой:{superpower} PP"
    def info(self):
        return "Этот покомон - боец\n\n " + super.info()

class Wizard(Pokemon):
    def info(self):
        return "Этот покомон - волшебник\n\n " + super.info()