from unittest import TestCase
import copy
import pytest

from env_agents_unlocker.envs.strategy_creation_env_agents.basic_strategy import (
    BasicStrategyCEA,
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


class TestBasicStrategyCEA(TestCase):
    def setUp(self):
        self.basic_strategy = BasicStrategyCEA(
            agents_kwargs=SETUP_AGENTS_KWARGS, name=SETUP_STRATEGY_NAME
        )

    def test_create_list_of_agents(self):
        assert len(self.basic_strategy.get_list_of_agents()) == SETUP_NB_AGENTS
        assert (
            len(self.basic_strategy.get_list_of_agents()[0].get_all_actions_names())
            == SETUP_NB_ACTION_TO_SELECT_BY_AGENT
        )

        # get the list of existing action
        temp_action_list = []
        for agent in self.basic_strategy.get_list_of_agents():
            temp_action_list += agent.get_all_actions_names()
        # make all actions unique
        action_list = list(set(temp_action_list))

        assert len(action_list) == SETUP_NB_AVAILABLE_ACTION_IN_ENV

    def test_create_new_agent_list(self):
        initial_list = self.basic_strategy.get_list_of_agents()
        assert initial_list == self.basic_strategy.get_list_of_agents()
        self.basic_strategy.create_new_agent_list()
        assert initial_list != self.basic_strategy.get_list_of_agents()

    def test_create_list_of_agents__missing_kwargs(self):
        missing_number_of_agent_kwargs = {
            "nb_available_action_in_env": SETUP_NB_AVAILABLE_ACTION_IN_ENV,
            "nb_action_to_select_by_agent": SETUP_NB_ACTION_TO_SELECT_BY_AGENT,
        }
        with pytest.raises(KeyError) as error:
            self.basic_strategy = BasicStrategyCEA(
                agents_kwargs=missing_number_of_agent_kwargs, name=SETUP_STRATEGY_NAME
            )
        assert SETUP_STRATEGY_NAME in str(error)
        assert "Missing 'agents_kwargs' element" in str(error)

        missing_nb_available_action_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_action_to_select_by_agent": SETUP_NB_ACTION_TO_SELECT_BY_AGENT,
        }
        with pytest.raises(KeyError) as error2:
            self.basic_strategy = BasicStrategyCEA(
                agents_kwargs=missing_nb_available_action_kwargs,
                name=SETUP_STRATEGY_NAME,
            )
        assert SETUP_STRATEGY_NAME in str(error2)
        assert "Missing 'agents_kwargs' element" in str(error2)

        missing_action_to_select_by_agent_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_available_action_in_env": SETUP_NB_AVAILABLE_ACTION_IN_ENV,
        }
        with pytest.raises(KeyError) as error3:
            self.basic_strategy = BasicStrategyCEA(
                agents_kwargs=missing_action_to_select_by_agent_kwargs,
                name=SETUP_STRATEGY_NAME,
            )
        assert SETUP_STRATEGY_NAME in str(error3)
        assert "Missing 'agents_kwargs' element" in str(error3)

    def test_equals(self):
        basic_strategy2 = BasicStrategyCEA(
            agents_kwargs=SETUP_AGENTS_KWARGS, name="basic_strategy"
        )

        assert self.basic_strategy == basic_strategy2

        basic_strategy2_name = copy.deepcopy(basic_strategy2)
        basic_strategy2_name.name += "2"
        assert not self.basic_strategy == basic_strategy2_name

    def test_hash(self):
        # test only on the action name, other value can be different
        basic_strategy2 = BasicStrategyCEA(
            agents_kwargs=SETUP_AGENTS_KWARGS, name="basic_strategy"
        )

        assert self.basic_strategy.__hash__() == basic_strategy2.__hash__()
        basic_strategy2.name += "2"
        assert not self.basic_strategy.__hash__() == basic_strategy2.__hash__()

    def test_str(self):
        assert str(SETUP_STRATEGY_NAME) in str(self.basic_strategy)
