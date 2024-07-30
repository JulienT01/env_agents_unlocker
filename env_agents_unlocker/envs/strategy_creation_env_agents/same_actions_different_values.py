from env_agents_unlocker.envs.env_agents.basic_agent_with_value import (
    BasicAgentWithValue,
)
from env_agents_unlocker.envs.env_agents.basic_agent import AbstractBaseAgent
from env_agents_unlocker.envs.actions.basic_action import BasicAction
from env_agents_unlocker.envs.strategy_creation_env_agents.abstract_strategy_creation_env_agents import (
    AbstractStrategyCreationEnvAgents,
)

import random


class SameActionsDifferentValuesStrategyCEA(AbstractStrategyCreationEnvAgents):
    def __init__(self, name="same_actions_different_values"):
        super().__init__(name=name)

    def create_list_of_agents(self, agents_kwargs: dict) -> list[AbstractBaseAgent]:
        """
        Get a list of basic agents that all have the same (locked) actions.
        It will be a list of BasicAgent, where each of them have the same list of BasicAction, but with different values for each action and agent

        ------------ Parameters ------------
        agents_kwargs (dict) :
            parameters specific to create these agents (and actions for theses agent). Here (key):
                - number_of_agents : the number of Agent in the returned list
                - nb_action_by_agent : the size of action list for each agent


        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment

        """
        # Extract the args in parameters
        number_of_agent_to_create = agents_kwargs["number_of_agents"]
        nb_action_by_agent = agents_kwargs["nb_action_by_agent"]

        agent_list = []

        # Create the agent with the specified number of action for each of them
        for i in range(number_of_agent_to_create):
            actions_for_this_agent = []
            for j in range(nb_action_by_agent):
                value = self._generate_random_value()
                actions_for_this_agent.append(
                    BasicAction(action_name=str(j), unlocked=False, value=value)
                )

            agent_list.append(
                BasicAgentWithValue(
                    name=str(i),
                    potential_actions=actions_for_this_agent,
                    pre_unlock_actions_names=None,
                )
            )
        return agent_list

    def _generate_random_value(self):
        return random.randint(0, 100)

    def __eq__(self, other):
        return (
            isinstance(other, SameActionsDifferentValuesStrategyCEA)
            and self.name == other.name
        )

    def __str__(self):
        return "\n strategy name : " + str(self.name)

    def __hash__(self):
        return self.name.__hash__()
