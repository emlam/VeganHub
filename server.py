from flask import Flask, render_template, request
import urllib2
import yelp_test
import json

from model import connect_to_db, db, Drink

app = Flask(__name__)

# routes up here


@app.route('/')
def home_page():
    """ Shows the home page """

    return render_template("homepage.html")


@app.route('/handle-search', methods=["POST"])
def handle_search():
    """Shows results from querying the yelp api"""

    #Get user inputted search term from landing page
    search_term = request.form.get("Search")

    #if user doesnt give us a location to search with, revert to default
    if request.form.get("zipcode"):
        location_term = request.form.get("zipcode")
    else:
        location_term = 'san francisco,ca'

    #Get what type of search user is doing based on selection from
    #drop down menu
    search_type = request.form.get("search_type")

    #Logic to see where search term should be sent to.
    if search_type == "Restaurants":
        api_result = restaurant_search_response(search_term, location_term)
    elif search_type == "Drinks":
        db_result = search_drink_db(search_term)
    else:
        print "nothing here, sorry. "

    #Making an empty dictionary to add values I want from Yelp response
    cleaned_data = {}

    #Iterating through the response to pull out information and place into
    #my new empty dictionary
    for i in range(len(api_result['businesses'])):
        b = api_result['businesses'][i]
        cleaned_data[b['name']] = {
                "name": b['name'],
                "address": b['location']['display_address'],
                "phone": b['display_phone'],
                "snippet_text": api_result['businesses'][i]['snippet_text'],
                "url": b['url']
            }

    # return render_template("restaurant-search-response.html", data=cleaned_data,
                                                    # term=search_term,
                                                    # location=location_term)

    return render_template('drink_search.html', tag=db_result)


#helper functions below


def restaurant_search_response(term, location):
    """ Get a Response from Yelp API """

    results = yelp_test.query_api(term, location)
    json_obj = urllib2.urlopen(results)
    data = json.load(json_obj)
    return data


def search_drink_db(tag):
    """ Search the drink db """

    #get form variables
    drink = Drink.query.filter_by(tag=tag).all()
    print "YOU MADE IT!!!!!!!!"
    return render_template('drink_search.html', tag=tag)


if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)

    app.run()
