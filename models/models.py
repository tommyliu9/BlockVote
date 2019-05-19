from app import db

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    poll_options = db.relationship('PollOption',backref='pollpost',lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Poll('{self.title}', '{self.poll_options}')"
class PollOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('poll.id'),nullable=False)
    def __repr__(self):
        return f"PollOption('{self.content}')"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique= True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    polls = db.relationship('Poll',backref='author', lazy=True)

    def __repr__(self):
        return f"User ('{self.email}', '{self.polls}')"

'''
Database test
'''
if __name__ == "__main__":
    db.create_all()
    user1 = User(email="Bob@gmail.com",password="fewfwef")
    db.session.add(user1)
    db.session.commit()
    poll = Poll(title="Is Donald trump a big gay?",user_id=user1.id )
    db.session.add(poll)
    db.session.commit()
    polop1 = PollOption(content="Yes",post_id=poll.id)
    polop2 = PollOption(content="No",post_id=poll.id)
    db.session.add(polop1)
    db.session.add(polop2)
    db.session.commit()
    print(User.query.all())