from server import db

class Account:
    def addTypeOfAccount(self, **kwargs):
        sql = "INSERT INTO account_types (user_id,user_type) VALUES(%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['user_type'])

        a = db.Cursor('photographyplatform', sql, sqldata)
        account = a.connect()

        if 'no results to fetch' in account:
            return '200'
        return '400'

    def getAccountType(self, id):
        sql = f"SELECT user_type FROM account_types WHERE user_id={id}"
        sqldata = ()

        t = db.Cursor('photographyplatform', sql, sqldata)
        type = t.connect()

        if len(type) > 0:
            for i in type:
                accountType = i.get('user_type')
            return accountType
        return '404'

    def addAboutToAccount(self, **kwargs):
        sql = "INSERT INTO abouts (user_id,about) VALUES(%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['about'])

        a = db.Cursor('photographyplatform', sql, sqldata)
        about = a.connect()

        if 'no resuluts to fetch' in about:
            return '200'
        return '400'

    def getAccountAbout(self, id):
        sql = f"SELECT about FROM abouts WHERE user_id={id}"
        sqldata = ()

        a = db.Cursor('photographyplatform', sql, sqldata)
        about = a.connect()

        if len(about) > 0:
            for i in about:
                accountAbout = i.get('about')
            return accountAbout
        return '404'

    def updateAbout(self, **kwargs):
        sql = "UPDATE abouts SET=%s WHERE id=%s"
        sqldata = (kwargs['about'],kwargs['id'])

        a = db.Cursor('photographyplatform', sql, sqldata)
        about = a.connect()

        if 'no resuluts to fetch' in about:
            return '200'
        return '400'

    def AddLinksToAccount(self, **kwargs):
        sql = "INSERT INTO links (user_id,link_name,link_url) VALUES(%s,%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['link_name'],kwargs['link_urk'])

        l = db.Cursor('photographyplatform', sql, sqldata)
        link = l.connect()

        if 'no resuluts to fetch' in link:
            return '200'
        return '400'
    
    def getAccountLinks(self, id):
        sql = f"SELECT link_name, link_url FROM links WHERE user_id={id}"
        sqldata = ()

        l = db.Cursor('photographyplatform', sql, sqldata)
        links = l.connect()

        accountLinks = {
            'links': []
        }

        if len(links) > 0:
            for i in links:
                accountLinks['links'].append('link_name')
                accountLinks['links'].append('link_url')
            return accountLinks
        return '404'

    def updateLinks(self, **kwargs):
        sql = "UPDATE links SET=%s, SET=%s WHERE id=%s"
        sqldata = (kwargs['link_name'],kwargs['link_url'],kwargs['id'])
    
    def addNoticeToAccount(self, **kwargs):
        sql = "INSERT INTO user_notices (user_id,message) VALUES(%s,%s)"
        sqldata = ()

        n = db.Cursor('photographyplatform', sql, sqldata)
        notice = n.connect()

        if 'no resuluts to fetch' in notice:
            return '200'
        return '400'

    def getAccountNotices(self, id):
        sql = f"SELECT message FROM user_notices WHERE user_id={id}"
        sqldata = ()

        n = db.Cursor('photographyplatform', sql, sqldata)
        notice = n.connect()

        accountMessges = {
            'messages': []
        }

        if len(notice) > 0:
            for i in notice:
                accountMessges['messages'].append('message')
            return accountMessges
        return '404'    

    def removeNotice(self, id):
        sql = f"DELETE FROM user_notices WHERE id={id}"
        sqldata = ()

        n = db.Cursor('photographyplatform', sql, sqldata)
        notice = n.connect()

        if 'no resuluts to fetch' in notice:
            return '200'
        return '400'

    def rateAccount(self, **kwargs):
        sql = "INSERT INTO photographer_ratings (user_id,photographer_id,rating) VALUES(%s,%s,%s)"
        sqldata = (kwargs['user_id'],kwargs['photographer_id'],kwargs['rating'])

        r = db.Cursor('photographyplatform', sql, sqldata)
        rate = r.connect()

        if 'no results to fetch' in rate:
            return '200'
        return '400'

    def getAccountRating(self, id):
        sql = f"SELECT AVG(rating) FROM photographer_ratings WHERE photographer_id={id}"
        sqldata = ()

        r = db.Cursor('photographyplatform', sql, sqldata)
        rating = r.connect()

        if len(rating) > 0:
            for i in rating:
                avgRating = i.get('rating')
            return avgRating
        return '404' 
    