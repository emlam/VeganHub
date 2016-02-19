""" Model & DB function for VeganHub Drink Search """

from flask_sqlalchemy import SQLAlchemy

#This makes the connection to Postgres

db = SQLAlchemy()

##############################################################################
# Model definitions


class Drink(db.Model):
    """ Wine information.  """

    __tablename__ = "drink"

    drink_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    drink_code = db.Column(db.String)
    company_name = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(450), nullable=True)
    tag = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Drink drink_code=%s tag=%s" % (self.drink_code, self.tag)

##############################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to Flask"""

    #Configuration to use Postgres Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///drinks'
    # app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = None
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience that will allow us to work with db directly.
    from server import app
    # from server import app
    connect_to_db(app)
    print "Connected to DB."
