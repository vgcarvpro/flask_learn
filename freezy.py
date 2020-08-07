from flask_frozen import Freezer
from flask_app import my_app

freezer = Freezer(my_app)

if __name__ == '__main__':
    freezer.freeze()