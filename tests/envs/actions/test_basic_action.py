from unittest import TestCase
import copy
from env_agents_unlocker.envs.actions.basic_action import BasicAction
from env_agents_unlocker.envs.actions.abstract_action import AbstractBaseAction

SETUP_ACTION_UNLOCKED_NAME = "test_action_unlocked"
SETUP_ACTION_UNLOCKED_VALUE = 42
SETUP_ACTION_UNLOCKED = True

SETUP_ACTION_LOCKED_NAME = "test_action_locked"
SETUP_ACTION_LOCKED_VALUE = 33
SETUP_ACTION_LOCKED = False


class TestBasicAction(TestCase):
    def setUp(self):
        self.action_unlocked = BasicAction(
            action_name=SETUP_ACTION_UNLOCKED_NAME,
            unlocked=SETUP_ACTION_UNLOCKED,
            value=SETUP_ACTION_UNLOCKED_VALUE,
        )
        self.action_locked = BasicAction(
            action_name=SETUP_ACTION_LOCKED_NAME,
            unlocked=SETUP_ACTION_LOCKED,
            value=SETUP_ACTION_LOCKED_VALUE,
        )

    def test_env_creation(self):
        # check the "setUp" action creation

        assert isinstance(self.action_unlocked, AbstractBaseAction)
        assert isinstance(self.action_unlocked, BasicAction)
        assert isinstance(self.action_locked, AbstractBaseAction)
        assert isinstance(self.action_locked, BasicAction)

        assert self.action_unlocked.action_name == SETUP_ACTION_UNLOCKED_NAME
        assert self.action_unlocked.unlocked == SETUP_ACTION_UNLOCKED
        assert self.action_unlocked.value == SETUP_ACTION_UNLOCKED_VALUE
        assert self.action_locked.action_name == SETUP_ACTION_LOCKED_NAME
        assert self.action_locked.unlocked == SETUP_ACTION_LOCKED
        assert self.action_locked.value == SETUP_ACTION_LOCKED_VALUE

    def test_unlock(self):
        assert not self.action_locked.unlocked
        self.action_locked.unlock()
        assert self.action_locked.unlocked

    def test_get_name(self):
        assert self.action_locked.get_name() == SETUP_ACTION_LOCKED_NAME

    def test_get_value(self):
        assert self.action_locked.get_value() == SETUP_ACTION_LOCKED_VALUE

    def test_is_unlock(self):
        assert self.action_locked.is_unlock() == SETUP_ACTION_LOCKED

    def test_to_dict(self):
        expected_value = {
            "name": self.action_locked.action_name,
            "unlock": self.action_locked.unlocked,
            "value": self.action_locked.value,
        }
        assert self.action_locked.to_dict() == expected_value

    def test_equals(self):
        action_locked2 = BasicAction(
            action_name=SETUP_ACTION_LOCKED_NAME,
            unlocked=SETUP_ACTION_LOCKED,
            value=SETUP_ACTION_LOCKED_VALUE,
        )
        assert self.action_locked == action_locked2

        action_locked2_name = copy.deepcopy(action_locked2)
        action_locked2_name.action_name += "2"
        assert not self.action_locked == action_locked2_name

        action_locked2_unlocked = copy.deepcopy(action_locked2)
        action_locked2_unlocked.unlocked = not SETUP_ACTION_LOCKED
        assert not self.action_locked == action_locked2_unlocked

        action_locked2_value = copy.deepcopy(action_locked2)
        action_locked2_value.value += 1
        assert not self.action_locked == action_locked2_value

    def test_hash(self):
        # test only on the action name, other value can be different
        action_locked2 = BasicAction(
            action_name=SETUP_ACTION_LOCKED_NAME, unlocked=True, value=101
        )
        assert self.action_locked.__hash__() == action_locked2.__hash__()
        action_locked2.action_name += "2"
        assert not self.action_locked.__hash__() == action_locked2.__hash__()

    def test_str(self):
        assert str(SETUP_ACTION_LOCKED_NAME) in str(self.action_locked)
        assert str(SETUP_ACTION_LOCKED_VALUE) in str(self.action_locked)
        assert str(SETUP_ACTION_LOCKED) in str(self.action_locked)
