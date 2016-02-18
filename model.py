""" Model & DB function for VeganHub Drink Search """

from flask_sqlalchemy import SQLAlchemy

#This makes the connection to Postgres

db = SQLAlchemy()

##############################################################################
# Model definitions


class Drink(db.Model):
    """ Wine information.  """

    __tablename__ = "drink"

    #drink_code options: w for wine, b for beer, l for liquor\
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    drink_code = db.Column(db.String)
    company_name = db.Columen(db.String(55), nullable=True)
    url = db.Column(db.String(100), nullable=True)
    tag = db.Column(db.String(65), nullable=False)
    notes = db.Column(db.String(400), nullable=True)
    status = db.Column(db.String(75), nullable=True)
    red_yellow_green = db.Column(db.String(65), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Drink drink_code=%s tag=%s" % (self.drink_code, self.tag)

##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to Flask"""

    #Configuration to use Postgres Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///drinks'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience that will allow us to work with db directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
