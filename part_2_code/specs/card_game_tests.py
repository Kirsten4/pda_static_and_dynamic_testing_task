import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_1 = Card('hearts', 4)
        self.card_2 = Card('spades', 10)
        self.card_3 = Card('diamonds', 1)
        self.card_game = CardGame()

    def test_check_for_ace__False(self):
        result = self.card_game.check_for_ace(self.card_1)
        self.assertEqual(False, result)

    def test_check_for_ace__True(self):
        result = self.card_game.check_for_ace(self.card_3)
        self.assertEqual(True, result)

    def test_check_for_highest_card__first_card_is_higher(self):
        result = self.card_game.highest_card(self.card_2, self.card_1)
        self.assertEqual(self.card_2, result)

    def test_check_for_highest_card__second_card_is_higher(self):
        result = self.card_game.highest_card(self.card_3, self.card_1)
        self.assertEqual(self.card_1, result)

    def test_check_cards_total(self):
        cards = [self.card_1,self.card_2,self.card_3]
        result = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 15", result)