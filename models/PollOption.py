from app import db

class PollOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('poll.id'),nullable=False)
    def __repr__(self):
        return f"PollOption('{self.content}')"