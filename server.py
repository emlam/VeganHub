from flask import Flask, render_template, request, jsonify
import urllib2
import yelp_test
import json

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


    return render_template("restaurant-search-response.html",data=api_result)

#helper functions below
def restaurant_search_response(term):
    """ Get a Response from Yelp API """

    results = yelp_test.query_api(term, 'san francisco')
    json_obj = urllib2.urlopen(results)
    data = json.load(json_obj)
    return data

    # results = yelp_test.query_api(term, 'san francisco')
    # json_obj = urllib2.urlopen(results)
    # read_data = json.loads(json_obj.read())
    # print read_data
    # # data = json.load(json_obj)
    # return read_data


def search_drink_db(term):
    """ Search the drink db """

    pass


if __name__ == '__main__':
    app.run(debug=True)
