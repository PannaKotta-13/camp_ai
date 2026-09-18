class Character:

  def __init__(self):
    self.name_character = ""
    self.class_character = ""
    self.hp_character = 0
    self.mana_character = 0

  # Добавили test_inputs=None. Если тесты передадут список, берем из него. Если нет — обычный input()
  def input_number(self, prompt_text, test_inputs=None):
    while True:
      try:
        if test_inputs is not None:
          val = test_inputs.pop(0)
        else:
          val = input(prompt_text)

        return int(val)
      except ValueError:
        print("Введите число!")

  def load_from_input(self, test_inputs=None):
    if test_inputs is not None:
      self.name_character = test_inputs.pop(0)
      self.class_character = test_inputs.pop(0)
      self.hp_character = self.input_number("Количество ХП: ", test_inputs)
      self.mana_character = self.input_number(
          "Уровень маны: ", test_inputs
      )
    else:
      self.name_character = input("Введите имя персонажа: ")
      self.class_character = input("Введите класс: ")
      self.hp_character = self.input_number("Количество ХП: ")
      self.mana_character = self.input_number("Уровень маны: ")

  def print_info(self):
    print("-" * 50)
    print("ДАННЫЕ О ПЕРСОНАЖЕ")
    print("-" * 50)
    print(
        f"Имя: {self.name_character}\nКласс: {self.class_character}\n"
        f"ХП: {self.hp_character}\nУровень маны: {self.mana_character}"
    )


if __name__ == "__main__":
  hero = Character()
  hero.load_from_input()
  hero.print_info()
