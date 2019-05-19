from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique= True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    polls = db.relationship('Poll',backref='author', lazy=True)

    def __repr__(self):
        return f"User ('{self.email}'"

db.create_all()