import pytest
import tasks
from tasks import Task


def equivalent(t1, t2):
    """Checks two tasks for equivalence"""
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing. Disconnect after"""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                  Task('wake', 'Brian'),
                                  Task('breathe', 'Tom', True),
                                  Task('exercise', 'Susan', False)])
def test_add_2(task):
    """Demonstrate parametrize with one parameter"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'Brian', False),
                          ('breathe', 'Tom', True)
                          ])
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters"""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(task, t_from_db)


tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'Brian'),
                Task('breathe', 'Tom', True),
                Task('exercise', 'Susan', False))


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    """Slightly different take."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


task_ids = ['Task({}, {}, {})'.format(t.summary, t.owner, t.done) for t in tasks_to_try]

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    """Demonstrate ids."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    """Demonstrate parametrize and test classes."""

    def test_equivalent(self, task):
        """Similar test in a class"""
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id

