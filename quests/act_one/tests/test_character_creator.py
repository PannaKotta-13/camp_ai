import pytest
from act_one.character_creator import Character

@pytest.mark.parametrize(
    "fake_inputs, expected_name, expected_class, expected_hp, expected_mana",
    [
        (["Маг", "Колдун", "100", "50"], "Маг", "Колдун", 100, 50),
        (["Воин", "Варвар", "250", "0"], "Воин", "Варвар", 250, 0),
        (
            ["Лучник", "Вор", "100", "30"],
            "Лучник",
            "Вор",
            100,
            30,
        ),
    ],
)
def test_character_load(
    fake_inputs, expected_name, expected_class, expected_hp, expected_mana
):
  hero = Character()

  hero.load_from_input(test_inputs=fake_inputs)

  assert hero.name_character == expected_name
  assert hero.class_character == expected_class
  assert hero.hp_character == expected_hp
  assert hero.mana_character == expected_mana