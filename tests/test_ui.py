import pytest
def test_homepage_loads():
    print("Opening browser to homepage...")
    assert "QA Application" in "Welcome to QA Application"