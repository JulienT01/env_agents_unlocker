from unittest import TestCase
import copy
from env_agents_unlocker.envs.actions.basic_action import BasicAction
from env_agents_unlocker.envs.env_agents.basic_agent_with_max_value import (
    BasicAgentWithMaxValue,
)
from env_agents_unlocker.envs.env_agents.abstract_base_agent import (
    AbstractBaseAgent,
)


SETUP_AGENT_NAME = "test_agent"
SETUP_INITIAL_LIST_ACTIONS = [
    BasicAction(action_name=str(j), unlocked=False, value=1) for j in range(5)
]

SETUP_AGENT_NAME_WITH_PRE_UNLOCK = "test_agent2"
SETUP_INITIAL_LIST_ACTIONS_WITH_PRE_UNLOCK = [
    BasicAction(action_name=str(j), unlocked=False, value=j) for j in range(3, 8)
]
SETUP_LIST_ACTIONS_TO_UNLOCK_WITH_PRE_UNLOCK = [
    SETUP_INITIAL_LIST_ACTIONS_WITH_PRE_UNLOCK[0],
    SETUP_INITIAL_LIST_ACTIONS_WITH_PRE_UNLOCK[2],
]
BEST_UNLOCKED_VALUE = max(x.value for x in SETUP_LIST_ACTIONS_TO_UNLOCK_WITH_PRE_UNLOCK)
SETUP_ALL_ACTION_NAME_WITH_PRE_UNLOCK = [
    action.action_name for action in SETUP_INITIAL_LIST_ACTIONS_WITH_PRE_UNLOCK
]
SETUP_LIST_ACTIONS_NAME_TO_UNLOCK_WITH_PRE_UNLOCK = [
    action.action_name for action in SETUP_LIST_ACTIONS_TO_UNLOCK_WITH_PRE_UNLOCK
]


class TestBasicAgentWithMaxValue(TestCase):
    def setUp(self):
        self.agent_basic = BasicAgentWithMaxValue(
            name=SETUP_AGENT_NAME,
            potential_actions=SETUP_INITIAL_LIST_ACTIONS,
            pre_unlock_actions_names=None,
        )
        self.agent_basic_pre_unlock = BasicAgentWithMaxValue(
            name=SETUP_AGENT_NAME_WITH_PRE_UNLOCK,
            potential_actions=SETUP_INITIAL_LIST_ACTIONS_WITH_PRE_UNLOCK,
            pre_unlock_actions_names=SETUP_LIST_ACTIONS_NAME_TO_UNLOCK_WITH_PRE_UNLOCK,
        )

    def test_env_creation(self):
        # check the "setUp" action creation
        assert isinstance(self.agent_basic, AbstractBaseAgent)
        assert isinstance(self.agent_basic, BasicAgentWithMaxValue)
        assert isinstance(self.agent_basic_pre_unlock, AbstractBaseAgent)
        assert isinstance(self.agent_basic_pre_unlock, BasicAgentWithMaxValue)

        assert self.agent_basic.name == SETUP_AGENT_NAME
        assert self.agent_basic.get_unlocked_actions_names() == []
        assert self.agent_basic.get_current_value() is None

        assert self.agent_basic_pre_unlock.name == SETUP_AGENT_NAME_WITH_PRE_UNLOCK
        assert (
            self.agent_basic_pre_unlock.get_unlocked_actions_names()
            == SETUP_LIST_ACTIONS_NAME_TO_UNLOCK_WITH_PRE_UNLOCK
        )
        assert self.agent_basic_pre_unlock.get_current_value() == BEST_UNLOCKED_VALUE

    def test_unlock_actions(self):
        agent_basic1 = copy.deepcopy(self.agent_basic)
        assert agent_basic1.get_unlocked_actions_names() == []
        assert agent_basic1.get_current_value() is None

        action_to_unlock1 = agent_basic1.get_all_actions_names()[0]
        agent_basic1.unlock_actions(action_to_unlock1)
        assert agent_basic1.get_unlocked_actions_names() == [action_to_unlock1]
        assert agent_basic1.get_current_value() is not None

        agent_basic2 = copy.deepcopy(self.agent_basic)
        assert agent_basic2.get_unlocked_actions_names() == []
        assert agent_basic2.get_current_value() is None

        actions_to_unlock2 = [
            agent_basic2.get_all_actions_names()[0],
            agent_basic2.get_all_actions_names()[2],
        ]
        agent_basic1.unlock_actions(actions_to_unlock2)
        assert agent_basic1.get_unlocked_actions_names() == actions_to_unlock2
        assert agent_basic1.get_current_value() is not None

    def test_get_all_actions_names(self):
        assert self.agent_basic.get_all_actions_names() == [
            action.action_name for action in SETUP_INITIAL_LIST_ACTIONS
        ]

    def test_to_dict(self):
        expected_value = {
            "name": self.agent_basic_pre_unlock.name,
            "all_actions": list(
                map(lambda x: x.to_dict(), SETUP_INITIAL_LIST_ACTIONS_WITH_PRE_UNLOCK)
            ),
            "unlocked_action": list(
                map(lambda x: x.to_dict(), SETUP_LIST_ACTIONS_TO_UNLOCK_WITH_PRE_UNLOCK)
            ),
        }
        assert self.agent_basic_pre_unlock.to_dict() == expected_value

    def test_get_current_value(self):
        assert self.agent_basic.get_current_value() is None
        assert self.agent_basic_pre_unlock.get_current_value() == BEST_UNLOCKED_VALUE

    def test_hash(self):
        # test only on the Agent name, other values can be different
        assert not self.agent_basic.__hash__() == self.agent_basic_pre_unlock.__hash__()
        self.agent_basic_pre_unlock.name = SETUP_AGENT_NAME
        assert self.agent_basic.__hash__() == self.agent_basic_pre_unlock.__hash__()

    def test_str(self):
        assert str(SETUP_AGENT_NAME_WITH_PRE_UNLOCK) in str(self.agent_basic_pre_unlock)
        assert str(SETUP_ALL_ACTION_NAME_WITH_PRE_UNLOCK) in str(
            self.agent_basic_pre_unlock
        )
        assert str(SETUP_LIST_ACTIONS_NAME_TO_UNLOCK_WITH_PRE_UNLOCK) in str(
            self.agent_basic_pre_unlock
        )
        assert str(BEST_UNLOCKED_VALUE) in str(self.agent_basic_pre_unlock)
