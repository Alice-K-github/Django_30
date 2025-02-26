import stripe
from config.settings import STRIPE_API_KEY


stripe.api_key = STRIPE_API_KEY


def create_stripe_price(pay_sum):
    # Создание цены в страйп
    return stripe.Price.create(
        currency='rub',
        unit_amount=pay_sum*100,
        recurring={"interval": "month"},
        product_data={"name": "Subscription"}
    )


def create_stripe_obj():
    # Создание продукта
    return stripe.Product.create(
        product_data={"name": "Subscription"}
    )


def create_stripe_session(price):
    # Создание сессии для получения ссылки на оплату
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 2}],
        mode='subscribtion'
    )
    return session.get("id"), session.get("url")
