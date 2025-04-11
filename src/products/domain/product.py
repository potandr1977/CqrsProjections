import queue
from datetime import datetime
from typing import Final, Optional

from src.products.domain.category import Category
from src.products.domain.price import Price

class Product:
    PRICE_MAX_SIZE: Final[int] = 10

    def __init__(self, sku:str, name:str, description:str, edit_date:datetime):
        self.__sku = sku
        self.__name = name
        self.__description = description
        self.__edit_date:datetime
        self.__categories = list[Category]()
        self.__base_price_history = queue.Queue[Price](maxsize=Product.PRICE_MAX_SIZE)

    @property
    def id(self):
        return self.__sku

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name:str):
        self.__name = new_name

    @property
    def prices(self) -> tuple[Price, ...]:
        return tuple(self.__base_price_history.queue)

    def add_price(self, price:Price):
        self.__base_price_history.queue.append(price)

    def add_category(self, category: Category):
        self.__categories.append(category)

    def replace_phrase(self, incoming_phrase:str, existing_phrase:str):
        trans_table = str.maketrans(existing_phrase, incoming_phrase)
        self.__name = self.__name.translate(trans_table)

    @staticmethod
    def create(name:str, description:str):
        sku = Product.__get_sku(name)
        product = Product(sku, name, description, datetime.now())
        return product

    @staticmethod
    def __get_sku(name:str):
        words = name.split()
        first_upper_words =[f"{word[0].upper()+word[1:]}" for word in words]
        skus_parts = [Product.__anti_vowel(word) for word in first_upper_words ]
        return ''.join(sku for sku in skus_parts)

    @staticmethod
    def __anti_vowel(text):
        return ''.join([letter for letter in text if letter not in 'aeiouy'])
