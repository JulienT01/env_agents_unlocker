from env_agents_unlocker.envs.env_agents.basic_agent import AbstractBaseAgent
from env_agents_unlocker.envs.actions.basic_action import BasicAction
from env_agents_unlocker.envs.strategy_creation_env_agents.abstract_strategy_creation_env_agents import (
    AbstractStrategyCreationEnvAgents,
)

import random


class SameActionsDifferentValuesWithNegativeValueStrategyCEA(
    AbstractStrategyCreationEnvAgents
):
    def __init__(
        self,
        agents_kwargs: dict,
        name="same_actions_different_values_with_negative",
        seed=None,
    ):
        """
        Create a list of agents that all have the same (locked) actions.
        It will be a list of BasicAgent, where each of them have the a list of BasicAction, but with different values for each action and agent. Some of this value can be negative.

        ------------ Parameters ------------
        agents_kwargs (dict) :
            parameters specific to create these agents (and actions for theses agent). Here (key):
                - number_of_agents (int) : the number of Agent in the returned list
                - nb_positive_action_by_agent (int): the number of action with positive value for each agent
                - nb_negative_action_by_agent (int): the number of action with negative value for each agent
                - agent_class (subclass of AbstractBaseAgent): class of expected agent to instantiate

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
        """
        sum_values = 0
        for agent in self.agent_list:
            agent_value = agent.get_current_value()
            if agent_value:
                sum_values += agent_value
        return sum_values

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

    def get_current_info(self):
        """
        what should be return as 'info' after a step or a reset in the environment (will be in the 'info' return, when the state is not 'terminated').
        here it's empty
        """
        return {}

    def create_new_agent_list(self):
        self.agent_list = self._create_list_of_agents()
        return self.agent_list

    def _create_list_of_agents(self) -> list[AbstractBaseAgent]:
        (
            number_of_agent_to_create,
            nb_positive_action_by_agent,
            nb_negative_action_by_agent,
            agent_class,
        ) = self._extract_kwargs(self.agents_kwargs)

        mask_action_pos_neg = (
            self._create_list_mask_matching_the_number_of_positive_and_negative(
                nb_positive_action_by_agent, nb_negative_action_by_agent
            )
        )

        agent_list = []
        # Create the agent with the specified number of action for each of them
        for i in range(number_of_agent_to_create):
            actions_for_this_agent = []
            for j in range(len(mask_action_pos_neg)):
                value = mask_action_pos_neg[j] * self._generate_random_value()
                actions_for_this_agent.append(
                    BasicAction(action_name=str(j), unlocked=False, value=value)
                )

            agent_list.append(
                agent_class(
                    name=str(i),
                    potential_actions=actions_for_this_agent,
                    pre_unlock_actions_names=None,
                )
            )
        return agent_list

    def _create_list_mask_matching_the_number_of_positive_and_negative(
        self, nb_positive, nb_negative
    ) -> list[bool]:
        total_action = nb_positive + nb_negative
        ratio_positive = nb_positive / total_action
        my_list = [random.random() > ratio_positive for _ in range(total_action)]

        if sum(my_list) != nb_positive:
            nb_to_change = abs(sum(my_list) - nb_positive)
            if sum(my_list) < nb_positive:
                # we should replace negative by positive
                list_index = [index for index, value in enumerate(my_list) if not value]
                index_to_change = random.sample(list_index, nb_to_change)
                for i in index_to_change:
                    my_list[i] = True
            else:
                # we should replace positive by negative
                list_index = [index for index, value in enumerate(my_list) if value]
                index_to_change = random.sample(list_index, nb_to_change)
                for i in index_to_change:
                    my_list[i] = False

        mask_list = [1 if val else -1 for val in my_list]
        return mask_list

    def _extract_kwargs(self, agents_kwargs):
        try:
            # Extract the args in parameters
            number_of_agent_to_create = agents_kwargs["number_of_agents"]
            nb_positive_action_by_agent = agents_kwargs["nb_positive_action_by_agent"]
            nb_negative_action_by_agent = agents_kwargs["nb_negative_action_by_agent"]
            agent_class = agents_kwargs["agent_class"]
            return (
                number_of_agent_to_create,
                nb_positive_action_by_agent,
                nb_negative_action_by_agent,
                agent_class,
            )
        except KeyError as err:
            error_message = (
                "Missing 'agents_kwargs' element for 'same_actions_different_values_with_negative' strategy : \n "
                + str(err)
            )
            print(error_message)
            raise KeyError(error_message)

    def _generate_random_value(self):
        return random.randint(0, 100)

    def __eq__(self, other):
        return (
            isinstance(other, SameActionsDifferentValuesWithNegativeValueStrategyCEA)
            and self.name == other.name
        )

    def __str__(self):
        return "\n strategy name : " + str(self.name)

    def __hash__(self):
        return self.name.__hash__()
