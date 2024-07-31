from unittest import TestCase
import copy
import pytest

from env_agents_unlocker.envs.strategy_creation_env_agents.same_actions_different_values import (
    SameActionsDifferentValuesStrategyCEA,
)

from env_agents_unlocker.envs.env_agents.basic_agent_with_max_value import (
    BasicAgentWithMaxValue,
)

SETUP_STRATEGY_NAME = "same_actions_different_values"

SETUP_NB_AGENTS = 5
SETUP_NB_ACTION_BY_AGENT = 3
SETUP_AGENTS_KWARGS = {
    "number_of_agents": SETUP_NB_AGENTS,
    "nb_action_by_agent": SETUP_NB_ACTION_BY_AGENT,
    "agent_class": BasicAgentWithMaxValue,
}


class TestSameActionsDifferentValuesStrategyCEA(TestCase):
    def setUp(self):
        self.s_a_d_v_strategy = SameActionsDifferentValuesStrategyCEA(
            agents_kwargs=SETUP_AGENTS_KWARGS, name=SETUP_STRATEGY_NAME
        )

    def test_create_list_of_agents(self):
        assert len(self.s_a_d_v_strategy.get_list_of_agents()) == SETUP_NB_AGENTS
        assert (
            len(self.s_a_d_v_strategy.get_list_of_agents()[0].get_all_actions_names())
            == SETUP_NB_ACTION_BY_AGENT
        )

    def test_create_list_of_agents__missing_kwargs(self):
        missing_number_of_agent_kwargs = {
            "nb_action_by_agent": SETUP_NB_ACTION_BY_AGENT,
            "agent_class": BasicAgentWithMaxValue,
        }
        with pytest.raises(KeyError) as error:
            self.s_a_d_v_strategy = SameActionsDifferentValuesStrategyCEA(
                agents_kwargs=missing_number_of_agent_kwargs, name=SETUP_STRATEGY_NAME
            )
        assert SETUP_STRATEGY_NAME in str(error)
        assert "Missing 'agents_kwargs' element" in str(error)

        missing_nb_of_action_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "agent_class": BasicAgentWithMaxValue,
        }
        with pytest.raises(KeyError) as error2:
            self.s_a_d_v_strategy = SameActionsDifferentValuesStrategyCEA(
                agents_kwargs=missing_nb_of_action_kwargs, name=SETUP_STRATEGY_NAME
            )
        assert SETUP_STRATEGY_NAME in str(error2)
        assert "Missing 'agents_kwargs' element" in str(error2)

        missing_agent_class_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_action_by_agent": SETUP_NB_ACTION_BY_AGENT,
        }
        with pytest.raises(KeyError) as error3:
            self.s_a_d_v_strategy = SameActionsDifferentValuesStrategyCEA(
                agents_kwargs=missing_agent_class_kwargs, name=SETUP_STRATEGY_NAME
            )
        assert SETUP_STRATEGY_NAME in str(error3)
        assert "Missing 'agents_kwargs' element" in str(error3)

    def test_equals(self):
        s_a_d_v_strategy2 = SameActionsDifferentValuesStrategyCEA(
            agents_kwargs=SETUP_AGENTS_KWARGS, name="same_actions_different_values"
        )

        assert self.s_a_d_v_strategy == s_a_d_v_strategy2

        basic_strategy2_name = copy.deepcopy(s_a_d_v_strategy2)
        basic_strategy2_name.name += "2"
        assert not self.s_a_d_v_strategy == basic_strategy2_name

    def test_hash(self):
        # test only on the action name, other value can be different
        s_a_d_v_strategy2 = SameActionsDifferentValuesStrategyCEA(
            agents_kwargs=SETUP_AGENTS_KWARGS, name="same_actions_different_values"
        )

        assert self.s_a_d_v_strategy.__hash__() == s_a_d_v_strategy2.__hash__()
        s_a_d_v_strategy2.name += "2"
        assert not self.s_a_d_v_strategy.__hash__() == s_a_d_v_strategy2.__hash__()

    def test_str(self):
        assert str(SETUP_STRATEGY_NAME) in str(self.s_a_d_v_strategy)
