from app import db

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    poll_options = db.relationship('PollOption',backref='pollpost',lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Poll('{self.title}')"