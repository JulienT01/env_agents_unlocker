from unittest import TestCase
import copy


from env_agents_unlocker.envs.strategy_creation_env_agents.same_actions_different_values import (
    SameActionsDifferentValuesStrategyCEA,
)

SETUP_STRATEGY_NAME = "same_actions_different_values"

SETUP_NB_AGENTS = 5
SETUP_NB_ACTION_BY_AGENT = 3
SETUP_AGENTS_KWARGS = {
    "number_of_agents": SETUP_NB_AGENTS,
    "nb_action_by_agent": SETUP_NB_ACTION_BY_AGENT,
}


class TestSameActionsDifferentValuesStrategyCEA(TestCase):
    def setUp(self):
        self.s_a_d_v_strategy = SameActionsDifferentValuesStrategyCEA(
            name=SETUP_STRATEGY_NAME
        )
        self.created_list = self.s_a_d_v_strategy.create_list_of_agents(
            SETUP_AGENTS_KWARGS
        )

    def test_create_list_of_agents(self):
        assert len(self.created_list) == SETUP_NB_AGENTS
        assert (
            len(self.created_list[0].get_all_actions_names())
            == SETUP_NB_ACTION_BY_AGENT
        )

    def test_equals(self):
        s_a_d_v_strategy2 = SameActionsDifferentValuesStrategyCEA(
            name="same_actions_different_values"
        )

        assert self.s_a_d_v_strategy == s_a_d_v_strategy2

        basic_strategy2_name = copy.deepcopy(s_a_d_v_strategy2)
        basic_strategy2_name.name += "2"
        assert not self.s_a_d_v_strategy == basic_strategy2_name

    def test_hash(self):
        # test only on the action name, other value can be different
        s_a_d_v_strategy2 = SameActionsDifferentValuesStrategyCEA(
            name="same_actions_different_values"
        )

        assert self.s_a_d_v_strategy.__hash__() == s_a_d_v_strategy2.__hash__()
        s_a_d_v_strategy2.name += "2"
        assert not self.s_a_d_v_strategy.__hash__() == s_a_d_v_strategy2.__hash__()

    def test_str(self):
        assert str(SETUP_STRATEGY_NAME) in str(self.s_a_d_v_strategy)
