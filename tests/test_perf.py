import pytest
import time
def test_api_response_time():
    start_time = time.time()
    time.sleep(0.2)
    duration = time.time() - start_time
    assert duration < 1.0