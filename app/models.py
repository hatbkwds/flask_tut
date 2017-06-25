from app import db

class Staff(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(142), nullable=False)
	lastname = db.Column(db.String(142), nullable=False)
	role = db.Column(db.String(16))
	slack = db.Column(db.String(16))
	email = db.Column(db.String(142))

	def __init__(self, firstname, lastname, role, slack, email):
		self.firstname = firstname
		self.lastname = lastname
		self.role = role
		self.slack = slack
		self.email = email

	def __repr__(self):
		return '<User %r>' % (self.firstname)