from unittest import TestCase
import pytest


from env_agents_unlocker.envs.env_factory import create_list_of_agents


class TestEnvFactory(TestCase):
    def test_create_list_of_agents__bad_agent_type(self):
        with pytest.raises(NotImplementedError):
            list_agent = create_list_of_agents(
                number_of_agent_to_create=5,
                type_of_agents="bad_type",
                agents_kwargs=None,
            )

    def test_create_list_of_agents__all_basic_type(self):
        nb_agent = 5
        number_of_action_to_select = 3
        number_of_action_max = 4

        agents_kwargs = {
            "number_of_action_max": number_of_action_max,
            "number_of_action_to_select": number_of_action_to_select,
        }

        list_agent = create_list_of_agents(
            number_of_agent_to_create=nb_agent,
            type_of_agents="all_basic",
            agents_kwargs=agents_kwargs,
        )

        assert len(list_agent) == nb_agent
        assert len(list_agent[0].get_all_actions_names()) == number_of_action_to_select

        # get the list of existing action
        temp_action_list = []
        for agent in list_agent:
            temp_action_list += agent.get_all_actions_names()
        # make all actions unique
        action_list = list(set(temp_action_list))

        assert len(action_list) == number_of_action_max
