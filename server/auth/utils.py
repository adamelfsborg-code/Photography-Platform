import bcrypt
from server import db



class User:
    def createUser(self, **kwargs):
        sql = "INSERT INTO users (fullname, email, password, profile_image, location) VALUES(%s,%s,%s,%s,%s)"
        sqldata = (kwargs['fullname'],kwargs['email'],kwargs['password'],kwargs['profile_image'],kwargs['location'])

        c = db.Cursor('photographyplatform', sql, sqldata)
        user = c.connect()

        if 'no results to fetch' in user:
            return '200'
        return '400'
        
    def hashPassword(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())
    
    def checkEmailExistence(self, email):
        sql = f"SELECT COUNT(id) FROM users WHERE email={email}"
        sqldata = ()

        c = db.Cursor('photographyplatform', sql, sqldata)
        existence = c.connect()

        if existence['count'] > 0:
            return '400'
        return '200'

    def loginUser(self, id, token):
        sql = f"UPDATE users SET token={token} WHERE id={id}"
        sqldata = ()

        l = db.Cursor('photographyplatform', sql, sqldata)
        loginUser = l.connect()

        if 'no resuluts to fetch' in loginUser:
            return '200'
        return '404'
    
    def checkEmailAndPasswordExistence(self, email,password):
        sql = f"SELECT id FROM users WHERE email={email} AND password={password}"
        sqldata = ()

        c = db.Cursor('photographyplatform', sql, sqldata)
        check = c.connect()

        if len(check) > 0:
            for i in check:
                id = i.get('id')            
            return id
        return '404'

    def checkPassword(self, password, hashed):
        if bcrypt.checkpw(password, hashed):
            return '200'
        return '400'

    def logoutUser(self, id):
        sql = f"UPDATE users SET token='null' WHERE id={id}"
        sqldata = ()

        l = db.Cursor('photographyplatform', sql, sqldata)
        logoutUser = l.connect()

        if 'no resuluts to fetch' in loginUser:
            return '200'
        return '404'
    

