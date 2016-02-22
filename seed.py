""" File to seed drinks database from Barnivore data  """

from sqlalchemy import func
from server import app
from model import Drink, connect_to_db, db
import json


def load_drink():
    """Load drink information into database."""

    file_list = ["seed_data/wine.json", "seed_data/beer.json", "seed_data/liquor.json"]
    for item_file_name in file_list:
        json_string = open(item_file_name).read()
        data = json.loads(json_string)

        # print "HERES THE DATA TYPE..", len(data)
        # print "heres the other thing..", type(data[0])

        for item in data:
            company = item['company']
            url = company['url']
            status = company['status']
            tag = company['tag']
            company_name = company['company_name']
            if item_file_name == "seed_data/wine.json":
                drink_code = "wine"
            elif item_file_name == "seed_data/beer.json":
                drink_code = "beer"
            else:
                drink_code = "liquor"

            drink = Drink(
                            drink_code=drink_code,
                            company_name=company_name,
                            url=url,
                            status=status,
                            tag=tag
                            )

            # We need to add to the session or it won't ever be stored
            db.session.add(drink)

#     # Once we're done, we should commit our work
    print "We are going to commit..."
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
# In case tables haven't been created, create them # db.create_all()
    load_drink()
