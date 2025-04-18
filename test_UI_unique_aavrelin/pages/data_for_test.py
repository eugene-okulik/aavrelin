from faker import Faker


fake = Faker()

expected_page = "Sale"
expected_promo = [
    {
        "title": "Pristine prices on pants, tanks and bras.",
        "info": "Women’s Deals",
        "more": "Shop Women’s Deals",
    },
    {
        "title": "Men’s Bargains",
        "info": "Stretch your budget with active attire",
        "more": "Shop Men’s Deals",
    },
    {
        "title": "Luma Gear Steals",
        "info": "Your best efforts deserve a deal",
        "more": "Shop Luma Gear",
    },
    {
        "title": "20% OFF",
        "info": "Every $200-plus purchase!",
        "more": None,
    },
    {
        "title": "Spend $50 or more — shipping is free!",
        "info": "Buy more, save more",
        "more": None,
    },
    {
        "title": "You can't have too many tees",
        "info": "4 tees for the price of 3. Right now",
        "more": "Tees on sale",
    },
]
error_password_message = (
    "Minimum length of this field must be equal or greater than 8 symbols."
    " Leading and trailing spaces will be ignored."
)
success_message = "Thank you for registering with Main Website Store."
filters = {
    "style": "Tee",
    "size": "XL",
    "climate": "Indoor",
    "color": "Blue"
}
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
password = fake.password
