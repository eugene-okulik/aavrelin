class Flowers:
    def __init__(self, name_flower, color, fresh, length, price, life):
        self.name_flower = name_flower
        self.color = color
        self.fresh = fresh
        self.length = length
        self.price = price
        self.life = life

    def __str__(self):
        return (f'{self.name_flower} ({self.color},'
                f' свежесть: {self.fresh} дней,'
                f' длина стебля: {self.length} см,'
                f' цена: {self.price} руб,'
                f' время жизни: {self.life} дней)')


class Flower1(Flowers):
    def __init__(self, name_flower, color, fresh, length, price, life=12):
        super().__init__(name_flower, color, fresh, length, price, life)


class Flower2(Flowers):
    def __init__(self, name_flower, color, fresh, length, price, life=22):
        super().__init__(name_flower, color, fresh, length, price, life)


class Flower3(Flowers):
    def __init__(self, name_flower, color, fresh, length, price, life=4):
        super().__init__(name_flower, color, fresh, length, price, life)


class Bouquet:
    def __init__(self):
        # букеты храним в списке
        self.list_flowers = []

    def add_flower(self, flower):
        self.list_flowers.append(flower)

    def cost(self):
        return sum(flower.price for flower in self.list_flowers)

    def avg_life(self):
        if not self.list_flowers:
            return 0
        return sum(flower.life for flower in self.list_flowers) / len(self.list_flowers)

    def __str__(self):
        return "\n".join(str(flower) for flower in self.list_flowers)


class Sorter:
    @staticmethod
    def sort_fresh(bouquet_flowers):
        return sorted(bouquet_flowers.list_flowers, key=lambda flower: flower.fresh)

    @staticmethod
    def sort_color(bouquet_flowers):
        return sorted(bouquet_flowers.list_flowers, key=lambda flower: flower.color)

    @staticmethod
    def sort_length(bouquet_flowers):
        return sorted(bouquet_flowers.list_flowers, key=lambda flower: flower.length)

    @staticmethod
    def sort_price(bouquet_flowers):
        return sorted(bouquet_flowers.list_flowers, key=lambda flower: flower.price)


bouquet = Bouquet()
flower1 = Flower1('Петуния', 'красный', 13, 50, 200, 5)
flower2 = Flower2('Тюльпан', 'желтый', 5, 40, 154, 8)
flower3 = Flower3('Роза', 'белый', 2, 0, 300, 11)
flower4 = Flower3('Гладиоус', 'фиолетовые', 2, 40, 550, 12)
flower5 = Flower3('Гвоздика', 'синий', 8, 64, 444, 22)

bouquet.add_flower(flower1)
bouquet.add_flower(flower2)
bouquet.add_flower(flower3)
bouquet.add_flower(flower4)
bouquet.add_flower(flower5)

print(bouquet)
print(f'\nСтоимость букета: {bouquet.cost()} руб')
print(f'\nСреднее время жизни букета: {bouquet.avg_life()} дней')

Sorter.sort_color(bouquet)
print('\nСортировка букета по цвету:')
print(bouquet)

lifetime = 5
print(f"\nПоиск цветов с временем жизни {lifetime} дней")
flower_life_find = [flower for flower in bouquet.list_flowers if flower.life == lifetime]
result_flower_life_find = '\n'.join(str(flower) for flower in flower_life_find)
print(result_flower_life_find)

name = 'Гвоздика'
print(f"\nПоиск цветка по имени {name}")
flower_name_find = [flower for flower in bouquet.list_flowers if flower.name_flower == name]
result_flower_name_find = '\n'.join(str(flower) for flower in flower_name_find)
print(result_flower_name_find)
