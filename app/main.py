from cinema.bar import CinemaBar
from cinema.hall import CinemaHall
from people.cinema_staff import Cleaner
from people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customers_list = [
        Customer(name=c["name"],
                 food=c["food"])
        for c in customers
    ]
    cleaner_cl = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)
    for customer_c in customers_list:
        CinemaBar.sell_product(
            customer=customer_c.name,
            product=customer_c.food
        )
    cinema_hall.movie_session(
        movie_name=movie,
        customers=customers_list,
        cleaning_staff=cleaner_cl
    )
    return None
