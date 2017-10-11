import os
basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = 'https://me.yahoo.com/a/p2juaOd9j_2Wc_BUmMc82VNsaI4gHTD14dfD5RPgBX5m2QZpmjJ8Psrf2cYBZMftYUBNggQ-'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://openid.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


