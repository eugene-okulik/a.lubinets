class Flowers:
    def __init__(self, country_of_origin, height, color, smell, cost, life_time, name):
        self.country_of_origin = country_of_origin
        self.height = height
        self.color = color
        self.smell = smell
        self.cost = cost
        self.life_time = life_time
        self.name = name

    def __str__(self):
        return (f"{self.name} Цвет: {self.color}, "
                f"Длина стебля: {self.height} см, "
                f"Стоимость: {self.cost}, "
                f"Время жизни: {self.life_time} дней")


class Bouquet:
    def __init__(self):
        self.flowers = []

    def collect_a_bouquet(self, flower):
        self.flowers.append(flower)

    def get_bouquet(self):
        return self.flowers

    def bouquet_price(self):
        return f"Цена букета: {sum(flower.cost for flower in self.flowers)}"

    def avg_time_bouquet(self):
        return f"Время увядания: {int(sum(flower.life_time for flower in self.flowers) / len(self.flowers))} дней"

    def sort_by_parameter(self, parameter):
        valid_parameters = ['cost', 'life_time', 'color', 'height']
        if parameter not in valid_parameters:
            print("Invalid sorting parameter!")
            return
        sorted_flowers = []

        if parameter == 'cost':
            sorted_flowers = sorted(self.flowers, key=lambda x: x.cost)
        elif parameter == 'life_time':
            sorted_flowers = sorted(self.flowers, key=lambda x: x.life_time)
        elif parameter == 'color':
            sorted_flowers = sorted(self.flowers, key=lambda x: x.color)
        elif parameter == 'height':
            sorted_flowers = sorted(self.flowers, key=lambda x: x.height)

        for flower in sorted_flowers:
            print(f"{flower.name}: {parameter} = {getattr(flower, parameter)}")

    def find_flowers_by_life_time(self, min_life_time):
        return [flower_local for flower_local in self.flowers if flower_local.life_time >= min_life_time]

    def __str__(self):
        return "\n".join(str(flower_local) for flower_local in self.flowers)


class Rose(Flowers):
    def __init__(self, country_of_origin, height, color, smell, bud_count, petal_count, mixed_color, cost, life_time,
                 name, freshness):
        super().__init__(country_of_origin, height, color, smell, cost, life_time, name)
        self.bud_count = bud_count
        self.petal_count = petal_count
        self.mixed_color = mixed_color
        self.freshness = freshness


class Lily(Flowers):
    def __init__(self, country_of_origin, height, color, smell, bud_count, cost, life_time, name, freshness):
        super().__init__(country_of_origin, height, color, smell, cost, life_time, name)
        self.bud_count = bud_count
        self.freshness = freshness


english_rose = Rose("Англия", 52, "красный", "устойчивый аромат", 1,
                    35, False, 300, 4, "Английская роза", "свежый")
floribunda_rose = Rose("Голландия", 60, "розовый", "менее выраженный аромат",
                       5, 19, False, 450, 5, "Флорибундская роза",
                       "удоволитворительно")
asiatic_lily_black = Lily("Тайланд", 110, "черный", "уверенно выраженный аромат",
                          15, 500, 8, "Азиатская черная лилия", "свежый")
asiatic_lily_pink = Lily("Тайланд", 98, "розово-красный",
                         "уверенно выраженный аромат", 15, 450, 8,
                         "Азиатская розовая лилия", "не свежый")


bouquet = Bouquet()
bouquet.collect_a_bouquet(english_rose)
bouquet.collect_a_bouquet(floribunda_rose)
bouquet.collect_a_bouquet(asiatic_lily_pink)
bouquet.collect_a_bouquet(asiatic_lily_black)
print(bouquet.bouquet_price())
print(bouquet.avg_time_bouquet())
bouquet.sort_by_parameter('cost')

min_life_time_value = 5
flowers_in_bouquet_with_long_life_time = bouquet.find_flowers_by_life_time(min_life_time=min_life_time_value)
print(f"\nЦветы в букете с временем жизни больше или равным {min_life_time_value} дней:")
for flower in flowers_in_bouquet_with_long_life_time:
    print(flower)
