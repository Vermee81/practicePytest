import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id():
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN tasks dbが初期化済みであるとすれば
    # WHEN 新しいタスクが追加された時に
    # THEN 返却されるtask_idはint型

    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

@pytest.mark.smoke
def test_added_task_has_id_set():
    """Make sure the task_id field is set by tasks.add()."""
    # GIVEN tasks_dbが初期化済みで
    #  AND 新しいタスクが追加されるとすれば
    new_task = Task('sit on a chair', owner='John', done=True)
    task_id = tasks.add(new_task)
    # WHEN タスクが取得された時に
    task_from_db = tasks.get(task_id)

    # THEN task_idはidフィールドと一致する
    assert task_from_db.id == task_id


def test_add_1():
    """tasks.get() using id returned from add() works."""
    task = Task('breathe', 'Brian', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                  Task('wake', 'Brian'),
                                  Task('breathe', 'Tom', True),
                                  Task('exercise', 'Susan', False)])
def test_add_2(task):
    """Demonstrate parametrize with one parameter"""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


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
