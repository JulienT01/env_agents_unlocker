from unittest import TestCase
import copy
import pytest

from env_agents_unlocker.envs.strategy_creation_env_agents.same_actions_different_values_with_negative_value import (
    SameActionsDifferentValuesWithNegativeValueStrategyCEA,
)

from env_agents_unlocker.envs.env_agents.basic_agent_with_cum_value import (
    BasicAgentWithCumValue,
)


SETUP_STRATEGY_NAME = "same_actions_different_values_with_negative"

SETUP_NB_AGENTS = 5
SETUP_NB_POS_ACTION_BY_AGENT = 3
SETUP_NB_NEG_ACTION_BY_AGENT = 7
SETUP_AGENTS_KWARGS = {
    "number_of_agents": SETUP_NB_AGENTS,
    "nb_positive_action_by_agent": SETUP_NB_POS_ACTION_BY_AGENT,
    "nb_negative_action_by_agent": SETUP_NB_NEG_ACTION_BY_AGENT,
    "agent_class": BasicAgentWithCumValue,
}


class TestSameActionsDifferentValuesStrategyCEA(TestCase):
    def setUp(self):
        self.s_a_d_v_w_n_v_strategy = (
            SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                agents_kwargs=SETUP_AGENTS_KWARGS, name=SETUP_STRATEGY_NAME
            )
        )

    def test_create_list_of_agents(self):
        assert len(self.s_a_d_v_w_n_v_strategy.get_list_of_agents()) == SETUP_NB_AGENTS
        assert (
            len(
                self.s_a_d_v_w_n_v_strategy.get_list_of_agents()[
                    0
                ].get_all_actions_names()
            )
            == SETUP_NB_POS_ACTION_BY_AGENT + SETUP_NB_NEG_ACTION_BY_AGENT
        )

    def test_create_strategy_with_more_positive(self):
        kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_positive_action_by_agent": 3,
            "nb_negative_action_by_agent": 7,
            "agent_class": BasicAgentWithCumValue,
        }
        strategy = SameActionsDifferentValuesWithNegativeValueStrategyCEA(
            agents_kwargs=kwargs, name=SETUP_STRATEGY_NAME
        )
        assert len(strategy.get_list_of_agents()) == SETUP_NB_AGENTS
        assert (
            len(strategy.get_list_of_agents()[0].get_all_actions_names())
            == SETUP_NB_POS_ACTION_BY_AGENT + SETUP_NB_NEG_ACTION_BY_AGENT
        )

    def test_create_list_mask_matching_the_number_of_positive_and_negative(self):
        pos_value = 4
        neg_value = 7
        result = self.s_a_d_v_w_n_v_strategy._create_list_mask_matching_the_number_of_positive_and_negative(
            pos_value, neg_value
        )
        assert sum(result) == pos_value - neg_value

        pos_value2 = 9
        neg_value2 = 3
        result = self.s_a_d_v_w_n_v_strategy._create_list_mask_matching_the_number_of_positive_and_negative(
            pos_value, neg_value
        )
        assert sum(result) == pos_value - neg_value

    def test_create_strategy_with_more_negative(self):
        kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_positive_action_by_agent": 7,
            "nb_negative_action_by_agent": 3,
            "agent_class": BasicAgentWithCumValue,
        }
        strategy = SameActionsDifferentValuesWithNegativeValueStrategyCEA(
            agents_kwargs=kwargs, name=SETUP_STRATEGY_NAME
        )
        assert len(strategy.get_list_of_agents()) == SETUP_NB_AGENTS
        assert (
            len(strategy.get_list_of_agents()[0].get_all_actions_names())
            == SETUP_NB_POS_ACTION_BY_AGENT + SETUP_NB_NEG_ACTION_BY_AGENT
        )

    def test_create_new_agent_list(self):
        initial_list = self.s_a_d_v_w_n_v_strategy.get_list_of_agents()
        assert initial_list == self.s_a_d_v_w_n_v_strategy.get_list_of_agents()
        self.s_a_d_v_w_n_v_strategy.create_new_agent_list()
        assert initial_list != self.s_a_d_v_w_n_v_strategy.get_list_of_agents()

    def test_create_list_of_agents__missing_kwargs(self):
        missing_number_of_agent_kwargs = {
            "nb_positive_action_by_agent": SETUP_NB_POS_ACTION_BY_AGENT,
            "nb_negative_action_by_agent": SETUP_NB_NEG_ACTION_BY_AGENT,
            "agent_class": BasicAgentWithCumValue,
        }
        with pytest.raises(KeyError) as error:
            self.s_a_d_v_w_n_v_strategy = (
                SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                    agents_kwargs=missing_number_of_agent_kwargs,
                    name=SETUP_STRATEGY_NAME,
                )
            )
        assert SETUP_STRATEGY_NAME in str(error)
        assert "Missing 'agents_kwargs' element" in str(error)

        missing_nb_of_pos_action_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_negative_action_by_agent": SETUP_NB_NEG_ACTION_BY_AGENT,
            "agent_class": BasicAgentWithCumValue,
        }
        with pytest.raises(KeyError) as error2:
            self.s_a_d_v_w_n_v_strategy = (
                SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                    agents_kwargs=missing_nb_of_pos_action_kwargs,
                    name=SETUP_STRATEGY_NAME,
                )
            )
        assert SETUP_STRATEGY_NAME in str(error2)
        assert "Missing 'agents_kwargs' element" in str(error2)

        missing_nb_of_neg_action_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_positive_action_by_agent": SETUP_NB_POS_ACTION_BY_AGENT,
            "agent_class": BasicAgentWithCumValue,
        }
        with pytest.raises(KeyError) as error3:
            self.s_a_d_v_w_n_v_strategy = (
                SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                    agents_kwargs=missing_nb_of_neg_action_kwargs,
                    name=SETUP_STRATEGY_NAME,
                )
            )
        assert SETUP_STRATEGY_NAME in str(error3)
        assert "Missing 'agents_kwargs' element" in str(error3)

        missing_agent_class_kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_positive_action_by_agent": SETUP_NB_POS_ACTION_BY_AGENT,
            "nb_negative_action_by_agent": SETUP_NB_NEG_ACTION_BY_AGENT,
        }
        with pytest.raises(KeyError) as error4:
            self.s_a_d_v_w_n_v_strategy = (
                SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                    agents_kwargs=missing_agent_class_kwargs, name=SETUP_STRATEGY_NAME
                )
            )
        assert SETUP_STRATEGY_NAME in str(error4)
        assert "Missing 'agents_kwargs' element" in str(error4)

    def test_compute_env_current_value(self):
        agent_number = 4
        kwargs = {
            "number_of_agents": SETUP_NB_AGENTS,
            "nb_positive_action_by_agent": SETUP_NB_POS_ACTION_BY_AGENT,
            "nb_negative_action_by_agent": SETUP_NB_NEG_ACTION_BY_AGENT,
            "agent_class": BasicAgentWithCumValue,
        }
        local_strategy = SameActionsDifferentValuesWithNegativeValueStrategyCEA(
            agents_kwargs=kwargs
        )

        expected_result = 0
        for agent in local_strategy.agent_list:
            expected_result += agent.potential_actions[0].get_value()
        assert local_strategy.compute_env_current_value() == 0
        for agent in local_strategy.agent_list:
            agent.unlock_actions("0")
        assert local_strategy.compute_env_current_value() == expected_result

    def test_get_final_results(self):
        assert (
            self.s_a_d_v_w_n_v_strategy.get_obs()
            == self.s_a_d_v_w_n_v_strategy.get_final_results()
        )

    def test_get_obs(self):
        expected_result = {
            "agents": list(
                map(lambda x: x.to_dict(), self.s_a_d_v_w_n_v_strategy.agent_list)
            )
        }
        assert self.s_a_d_v_w_n_v_strategy.get_obs() == expected_result

    def test_equals(self):
        s_a_d_v_w_n_v_strategy2 = (
            SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                agents_kwargs=SETUP_AGENTS_KWARGS,
                name="same_actions_different_values_with_negative",
            )
        )

        assert self.s_a_d_v_w_n_v_strategy == s_a_d_v_w_n_v_strategy2

        basic_strategy2_name = copy.deepcopy(s_a_d_v_w_n_v_strategy2)
        basic_strategy2_name.name += "2"
        assert not self.s_a_d_v_w_n_v_strategy == basic_strategy2_name

    def test_hash(self):
        # test only on the action name, other value can be different
        s_a_d_v_w_n_v_strategy2 = (
            SameActionsDifferentValuesWithNegativeValueStrategyCEA(
                agents_kwargs=SETUP_AGENTS_KWARGS,
                name="same_actions_different_values_with_negative",
            )
        )

        assert (
            self.s_a_d_v_w_n_v_strategy.__hash__() == s_a_d_v_w_n_v_strategy2.__hash__()
        )
        s_a_d_v_w_n_v_strategy2.name += "2"
        assert (
            not self.s_a_d_v_w_n_v_strategy.__hash__()
            == s_a_d_v_w_n_v_strategy2.__hash__()
        )

    def test_str(self):
        assert str(SETUP_STRATEGY_NAME) in str(self.s_a_d_v_w_n_v_strategy)
