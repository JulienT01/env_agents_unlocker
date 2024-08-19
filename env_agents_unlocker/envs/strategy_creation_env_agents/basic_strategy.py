from env_agents_unlocker.envs.env_agents.basic_agent import BasicAgent
from env_agents_unlocker.envs.env_agents.basic_agent import AbstractBaseAgent
from env_agents_unlocker.envs.actions.basic_action import BasicAction
from env_agents_unlocker.envs.strategy_creation_env_agents.abstract_strategy_creation_env_agents import (
    AbstractStrategyCreationEnvAgents,
)

import random


class BasicStrategyCEA(AbstractStrategyCreationEnvAgents):
    def __init__(self, agents_kwargs: dict, name="basic_strategy", seed=None):
        """
        Create a list of basic agents that all have the same kind of basic (locked) actions.
        It will be a list of BasicAgent, where each of them have a list of BasicAction  (subpart of all the same BasicAction available).

        ------------ Parameters ------------
        agents_kwargs (dict) :
            parameters specific to create these agents (and actions for theses agent). Here (key):
                - nb_available_action_in_env (int): the size of all available actions
                - nb_action_to_select_by_agent (int): the size of action list for each agent
                - number_of_agents (int): the number of Agent in the returned list

        seed (int) :
            to manage reproducibility

        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment

        """
        super().__init__(agents_kwargs=agents_kwargs, name=name)
        random.seed(seed)
        self.agent_list = self._create_list_of_agents()

    def get_list_of_agents(self) -> list[AbstractBaseAgent]:
        """
            Get the list of agent created by the strategy
        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment
        """
        return self.agent_list

    def compute_env_current_value(self):
        """
        The value of the current state of the env is the sum of the agents current value
        ------------ Returns ---------------
        Dict of the agents
        """
        sum_rewards = 0
        for agent in self.agent_list:
            sum_rewards += agent.get_current_value()
        return sum_rewards

    def get_obs(self):
        """
        observation of the current state of the environment.
        """
        return {"agents": list(map(lambda x: x.to_dict(), self.agent_list))}

    def get_final_results(self):
        """
        'final state' of the environment (will be in the 'info' return, when the state is 'terminated')
        here it's the same as the get_obs().
        """
        return self.get_obs()

    def create_new_agent_list(self):
        self.agent_list = self._create_list_of_agents()
        return self.agent_list

    def _create_list_of_agents(
        self,
    ) -> list[AbstractBaseAgent]:
        (
            number_of_agent_to_create,
            nb_available_action_in_env,
            nb_action_to_select_by_agent,
        ) = self._extract_kwargs(self.agents_kwargs)

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

    def _extract_kwargs(self, agents_kwargs):
        try:
            # Extract the args in parameters
            number_of_agent_to_create = agents_kwargs["number_of_agents"]
            nb_available_action_in_env = agents_kwargs["nb_available_action_in_env"]
            nb_action_to_select_by_agent = agents_kwargs["nb_action_to_select_by_agent"]
            return (
                number_of_agent_to_create,
                nb_available_action_in_env,
                nb_action_to_select_by_agent,
            )
        except KeyError as err:
            error_message = (
                "Missing 'agents_kwargs' element for 'basic_strategy' : \n " + str(err)
            )
            print(error_message)
            raise KeyError(error_message)

    def __eq__(self, other):
        return isinstance(other, BasicStrategyCEA) and self.name == other.name

    def __str__(self):
        return "\n strategy name : " + str(self.name)

    def __hash__(self):
        return self.name.__hash__()
