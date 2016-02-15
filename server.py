from flask import Flask, render_template, request, jsonify
import urllib2
import yelp_test
import json
import pprint

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
    search_type = request.form.get("search_type")

    if search_type == "Restaurants":
        api_result = restaurant_search_response(search_term)

    cleaned_data = {}

    for i in range(len(api_result['businesses'])):
        cleaned_data[api_result['businesses'][i]['name']] = {
                "address": api_result['businesses'][i]['location']['display_address'],
                "phone": api_result['businesses'][i]['display_phone'],
                "snippet_text": api_result['businesses'][i]['snippet_text'],
            }


    print "Here is your new cleaned data:", cleaned_data

    return render_template("restaurant-search-response.html", data=cleaned_data,
                                                            term=search_term)

#helper functions below
def restaurant_search_response(term):
    """ Get a Response from Yelp API """

    results = yelp_test.query_api(term, 'san francisco')
    json_obj = urllib2.urlopen(results)
    data = json.load(json_obj)
    return data


def search_drink_db(term):
    """ Search the drink db """

    pass


if __name__ == '__main__':
    app.run(debug=True)
