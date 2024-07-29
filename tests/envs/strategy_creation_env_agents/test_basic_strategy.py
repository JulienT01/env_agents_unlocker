from unittest import TestCase
import copy


from env_agents_unlocker.envs.strategy_creation_env_agents.basic_strategy import (
    BasicStrategyCreationEnvAgents,
)

SETUP_STRATEGY_NAME = "basic_strategy"

SETUP_NB_AGENTS = 5
SETUP_NB_AVAILABLE_ACTION_IN_ENV = 4
SETUP_NB_ACTION_TO_SELECT_BY_AGENT = 3
SETUP_AGENTS_KWARGS = {
    "number_of_agents": SETUP_NB_AGENTS,
    "nb_available_action_in_env": SETUP_NB_AVAILABLE_ACTION_IN_ENV,
    "nb_action_to_select_by_agent": SETUP_NB_ACTION_TO_SELECT_BY_AGENT,
}


class TestBasicStrategyCreationEnvAgents(TestCase):
    def setUp(self):
        self.basic_strategy = BasicStrategyCreationEnvAgents(name=SETUP_STRATEGY_NAME)
        self.created_list = self.basic_strategy.create_list_of_agents(
            SETUP_AGENTS_KWARGS
        )

    def test_create_list_of_agents(self):
        assert len(self.created_list) == SETUP_NB_AGENTS
        assert (
            len(self.created_list[0].get_all_actions_names())
            == SETUP_NB_ACTION_TO_SELECT_BY_AGENT
        )

        # get the list of existing action
        temp_action_list = []
        for agent in self.created_list:
            temp_action_list += agent.get_all_actions_names()
        # make all actions unique
        action_list = list(set(temp_action_list))

        assert len(action_list) == SETUP_NB_AVAILABLE_ACTION_IN_ENV

    def test_equals(self):
        basic_strategy2 = BasicStrategyCreationEnvAgents(name="basic_strategy")

        assert self.basic_strategy == basic_strategy2

        basic_strategy2_name = copy.deepcopy(basic_strategy2)
        basic_strategy2_name.name += "2"
        assert not self.basic_strategy == basic_strategy2_name

    def test_hash(self):
        # test only on the action name, other value can be different
        basic_strategy2 = BasicStrategyCreationEnvAgents(name="basic_strategy")

        assert self.basic_strategy.__hash__() == basic_strategy2.__hash__()
        basic_strategy2.name += "2"
        assert not self.basic_strategy.__hash__() == basic_strategy2.__hash__()

    def test_str(self):
        assert str(SETUP_STRATEGY_NAME) in str(self.basic_strategy)
