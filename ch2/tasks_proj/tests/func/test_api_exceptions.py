import pytest
import tasks


def test_add_raises():
    """add() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.add(task='Not a Task Object')


@pytest.mark.smoke
def test_list_tasks_raises():
    """list_tasks() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=22)

