from env_agents_unlocker.envs.env_agents.basic_agent import BasicAgent
from env_agents_unlocker.envs.env_agents.basic_agent import AbstractBaseAgent
from env_agents_unlocker.envs.actions.basic_action import BasicAction
from env_agents_unlocker.envs.strategy_creation_env_agents.abstract_strategy_creation_env_agents import (
    AbstractStrategyCreationEnvAgents,
)

import random


class BasicStrategyCEA(AbstractStrategyCreationEnvAgents):
    def __init__(self, name="basic_strategy"):
        super().__init__(name=name)

    def create_list_of_agents(self, agents_kwargs: dict) -> list[AbstractBaseAgent]:
        """
        Get a list of basic agents that all have the same kind of basic (locked) actions.
        It will be a list of BasicAgent, where each of them have a list of BasicAction  (subpart of all the same BasicAction available).

        ------------ Parameters ------------
        agents_kwargs (dict) :
            parameters specific to create these agents (and actions for theses agent). Here (key):
                - nb_available_action_in_env : the size of all available actions
                - nb_action_to_select_by_agent : the size of action list for each agent
                - number_of_agents : the number of Agent in the returned list


        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment

        """
        # Extract the args in parameters
        number_of_agent_to_create = agents_kwargs["number_of_agents"]
        nb_available_action_in_env = agents_kwargs["nb_available_action_in_env"]
        nb_action_to_select_by_agent = agents_kwargs["nb_action_to_select_by_agent"]

        basic_agent_list = []

        # Create all the possible action for these agents
        available_actions = []
        for j in range(nb_available_action_in_env):
            available_actions.append(
                BasicAction(action_name=str(j), unlocked=False, value=1)
            )

        # Create the agent with the specified number of action for each of them
        for i in range(number_of_agent_to_create):
            actions_for_this_agent = random.sample(
                available_actions, nb_action_to_select_by_agent
            )

            basic_agent_list.append(
                BasicAgent(
                    name=str(i),
                    potential_actions=actions_for_this_agent,
                    pre_unlock_actions_names=None,
                )
            )
        return basic_agent_list

    def __eq__(self, other):
        return isinstance(other, BasicStrategyCEA) and self.name == other.name

    def __str__(self):
        return "\n strategy name : " + str(self.name)

    def __hash__(self):
        return self.name.__hash__()
