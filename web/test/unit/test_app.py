import unittest.mock
from redis import ConnectionError


@unittest.mock.patch("page_tracker.app.redis")
def test_should_call_redis_incr(mock_redis, http_client):
    #Given 
    # mock_redis.return_value.incr.return_value = 5
    mock_redis.return_value.incr.side_effect = ConnectionError
    
    #when 
    response = http_client.get('/')
    
    #then 
    # assert response.status_code == 200
    # assert response.text == 'This page has been seen 5 times.'
    # mock_redis.return_value.incr.assert_called_once_with("page_views")
    assert response.status_code == 500
    assert response.text == "Sorry, something went wrong \N{pensive face}"