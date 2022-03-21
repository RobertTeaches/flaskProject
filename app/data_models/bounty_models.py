from app import db
static_id = 0

class Bounty(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(1024), index=True, unique=True)
    reward = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    image_src = db.Column(db.String(256))

    def __init__(self, title="N/A", description="Empty", reward=1, xp=25):
        global  static_id
        self.id = static_id
        static_id += 1
        self.title = title
        self.description = description
        self.reward = reward
        self.xp = xp

    def __repr__(self):
        return f"Bounty: {self.title} - {self.id}"

