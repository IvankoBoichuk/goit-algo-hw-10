from pulp import LpMaximize, LpProblem, LpVariable

# 1. Створення задачі лінійного програмування для максимізації
model = LpProblem(name="beverage-production-optimization", sense=LpMaximize)

# 2. Оголошення змінних, які представляють кількість вироблених одиниць "Лимонаду" та "Фруктового соку"
Lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
FruitJuice = LpVariable(name="FruitJuice", lowBound=0, cat="Integer")

# 3. Додавання цільової функції: максимізація кількості вироблених одиниць "Лимонаду" та "Фруктового соку"
model += Lemonade + FruitJuice, "Total_Production"

# 4. Додавання обмежень на ресурси
model += (2 * Lemonade + 1 * FruitJuice <= 100, "Water_Constraint")            # Вода
model += (1 * Lemonade <= 50, "Sugar_Constraint")                              # Цукор
model += (1 * Lemonade <= 30, "LemonJuice_Constraint")                         # Лимонний сік
model += (2 * FruitJuice <= 40, "FruitPuree_Constraint")                       # Фруктове пюре

# 5. Розв'язання задачі
model.solve()

# 6. Виведення результатів
lemonade_production = Lemonade.varValue
fruitjuice_production = FruitJuice.varValue
total_production = lemonade_production + fruitjuice_production

print(lemonade_production, fruitjuice_production, total_production)