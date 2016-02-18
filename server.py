from flask import Flask, render_template, request
import urllib2
import yelp_test
import json
import os

app = Flask(__name__)

# routes up here


@app.route('/')
def home_page():
    """ Shows the home page """

    return render_template("homepage.html")


@app.route('/handle-search', methods=["POST"])
def handle_search():
    """Shows results from querying the yelp api"""

    search_term = request.form.get("Search")

    if request.form.get("zipcode"):
        location_term = request.form.get("zipcode")
    else:
        location_term = 'san francisco,ca'

    search_type = request.form.get("search_type")

    if search_type == "Restaurants":
        api_result = restaurant_search_response(search_term, location_term)

    cleaned_data = {}

    for i in range(len(api_result['businesses'])):
        cleaned_data[api_result['businesses'][i]['name']] = {
                "name": api_result['businesses'][i]['name'],
                "address": api_result['businesses'][i]['location']['display_address'],
                "phone": api_result['businesses'][i]['display_phone'],
                "snippet_text": api_result['businesses'][i]['snippet_text'],
                "url": api_result['businesses'][i]['url']
            }

    print "Here is your new cleaned data:", cleaned_data

    return render_template("restaurant-search-response.html", data=cleaned_data,
                                                    term=search_term,
                                                    location=location_term)

#helper functions below


def restaurant_search_response(term, location):
    """ Get a Response from Yelp API """

    results = yelp_test.query_api(term, location)
    json_obj = urllib2.urlopen(results)
    data = json.load(json_obj)
    return data


def search_drink_db(term):
    """ Search the drink db """

    pass


if __name__ == '__main__':
    app.run(debug=True)
