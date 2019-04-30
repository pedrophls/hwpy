from nose.tools import *
from app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get("/", follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get("/form", follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill out this form", rv.data)

    data = {'name':'Peter', 'greet':'Mr'}
    rv = web.post('/form', follow_redirects=True, data=data)
    assert_in(b"Peter", rv.data)
    assert_in(b"Mr", rv.data)