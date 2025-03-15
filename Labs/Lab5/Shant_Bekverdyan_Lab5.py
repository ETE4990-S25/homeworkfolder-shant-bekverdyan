# %% [markdown]
# Used Alex Akasaka's Lab3 code to conduct unit test.

# %%
import unittest
import json
import os

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_name = "TestPlayer"
        self.player_type_warrior = "warrior"
        self.player_type_mage = "mage"
        self.player_type_assassin = "assassin"

    def tearDown(self):
        try:
            os.remove(f"{self.player_name}.json")
        except FileNotFoundError:
            pass

    def test_player_initialization_warrior(self):
        player = Player(self.player_name, self.player_type_warrior)
        self.assertEqual(player.name, self.player_name)
        self.assertEqual(player.player_type, self.player_type_warrior)
        self.assertEqual(player.attributes, {"health": 100, "attack": 50, "defense": 20})
        self.assertEqual(player.items, [])

    def test_player_initialization_mage(self):
        player = Player(self.player_name, self.player_type_mage)
        self.assertEqual(player.name, self.player_name)
        self.assertEqual(player.player_type, self.player_type_mage)
        self.assertEqual(player.attributes, {"health": 80, "attack": 70, "defense": 10})
        self.assertEqual(player.items, [])

    def test_player_initialization_assassin(self):
        player = Player(self.player_name, self.player_type_assassin)
        self.assertEqual(player.name, self.player_name)
        self.assertEqual(player.player_type, self.player_type_assassin)
        self.assertEqual(player.attributes, {"health": 60, "attack": 80, "defense": 5})
        self.assertEqual(player.items, [])

    def test_set_attributes_warrior(self):
        player = Player(self.player_name, self.player_type_warrior)
        attributes = player.set_attributes(self.player_type_warrior)
        self.assertEqual(attributes, {"health": 100, "attack": 50, "defense": 20})

    def test_set_attributes_mage(self):
        player = Player(self.player_name, self.player_type_mage)
        attributes = player.set_attributes(self.player_type_mage)
        self.assertEqual(attributes, {"health": 80, "attack": 70, "defense": 10})

    def test_set_attributes_assassin(self):
        player = Player(self.player_name, self.player_type_assassin)
        attributes = player.set_attributes(self.player_type_assassin)
        self.assertEqual(attributes, {"health": 60, "attack": 80, "defense": 5})

    def test_save_profile(self):
        player = Player(self.player_name, self.player_type_warrior)
        player.items = ["sword", "shield"]
        player.save_profile(self.player_type_warrior)

        with open(f"{self.player_name}.json", "r") as file:
            data = json.load(file)

        self.assertEqual(data["name"], self.player_name)
        self.assertEqual(data["player_type"], self.player_type_warrior)
        self.assertEqual(data["attributes"], {"health": 100, "attack": 50, "defense": 20})
        self.assertEqual(data["items"], ["sword", "shield"])

if __name__ == '__main__':
    unittest.main(argv=['First argument ignored'], exit=False)


