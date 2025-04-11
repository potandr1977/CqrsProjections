from src.carts.domain.cart_item import CartItem
from src.products.domain.product import Product


class Cart:
    def __init__(self, id:int, name:str, description:str):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__items:set[CartItem] = set[CartItem]()

    @property
    def get_items(self)->tuple[CartItem, ...]:
        return tuple(self.__items)

    def add_item(self, product:Product, amount: int):
        product_ids = set([ci.product.id() for ci in self.__items])
        if  product.id() in product_ids:
            raise ValueError(f"The product {product.name} is already in a cart.")

        cart_item = CartItem(product,amount)
        self.__items.add(cart_item)

        return cart_item

    def remove_item(self, cart_item:CartItem)->tuple[CartItem, ...]:
        if not cart_item in self.__items:
            raise ValueError(f"Item {cart_item.__repr__()} not found. Can't delete cart item.")

        self.__items.remove(cart_item)

        return tuple(self.__items)

    def remove_item_by_product_id(self, product_id:int)->tuple[CartItem, ...]:
        cart_item = next((ci for ci in self.__items if ci.product.id() == product_id), None)
        if cart_item is None:
            raise ValueError(f"Item with product id {product_id} not found. Can't delete cart item by product id.")
        self.__items.remove(cart_item)
        return tuple(self.__items)

    def set_amount_by_product_id(self, product_id:int, new_amount:int):
        cart_item = next((ci for ci in self.__items if ci.product.id() == product_id), None)
        if cart_item is None:
            raise ValueError(f"Item with product id {product_id} not found. Can't set amount by product id.")
        cart_item.amount = new_amount
        return cart_item
