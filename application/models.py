from application import db

class RecordDB(db.Model):
    """ Datamodel for an audio record broadcasted realtime """

    __tablename__ = "audio record"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    artist = db.Column(db.String(256))
    album = db.Column(db.String(256))
    started_at = db.Column(db.DateTime) 
    added_at = db.Column(db.DateTime) # these two should be basically the same time.. 

    def __repr__(self):
        return f"<{self.title} - {self.artist}>"


class LogDB(db.Model):
    """ Datamodel for recording logs from filesystem """

    __tablename__ = "access log"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(256), nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<{self.message}>"
