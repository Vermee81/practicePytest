from tasks import Task


def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'Okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'Okken',
                'done': True,
                'id': 21}
    assert t_dict == expected

def test_replace():
    """_replace() should change passed in fields"""
    t_before = Task('do something', 'Taro', False, 22)
    t_after= t_before._replace(summary='replaced summary', done = True)
    t_expected = Task('replaced summary', 'Taro', True, 22)
    assert t_after == t_expected

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of named tuple."""
    t = Task('buy milk', 'Hanako', False)
    assert t.summary == 'buy milk'
    assert t.owner == 'Hanako'
    assert t.done == False