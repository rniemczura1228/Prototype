# content of test_sysexit.py
import pytest

# test modification/commit
def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
