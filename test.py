from app import app #getting info from the file

def test1():
  pass
    """
    This function tests that the application has a correct response code when the application goes live.
    """

    response = app.test_clients().get('/')
    assert response.status_code == 200


def test2():
  pass

    response = app.test_clients().get('/edit')
    assert response.status_code == 200

def test3():
  pass
