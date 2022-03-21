from app import app, render_template
from app.data_models.bounty_models import Bounty
from app.utils import *

#App Globals
bounties = []


@app.route('/')
def home():  # put application's code here
    global bounties
    if len(bounties) == 0:
        bounties = get_bounties()
    return render_template("index.html", bounties=bounties)


if __name__ == '__main__':
    app.run(debug=True)
