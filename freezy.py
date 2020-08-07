from Flask_Frozen import Freezer
from flask_app import my_app

freezer = Freezer(my_app)

if __name__ == '__main__':
    freezer.freeze()