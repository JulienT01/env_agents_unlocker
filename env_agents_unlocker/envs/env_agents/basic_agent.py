from env_agents_unlocker.envs.env_agents.abstract_base_agent import (
    AbstractBaseAgent,
)
from env_agents_unlocker.envs.actions.basic_action import AbstractBaseAction


class BasicAgent(AbstractBaseAgent):
    def __init__(
        self,
        name: str,
        potential_actions: list[AbstractBaseAction],
        pre_unlock_actions_names: list[str] = None,
    ) -> None:
        """
        Basic Agent, its objective (to maximize its value) is to unlock the maximum of its actions
        ------------ Parameters ------------
        name (str):
            The name of the agent (could be use as ID)
        potential_actions (list[AbstractBaseAction]):
            List of all the actions for this agent (lock and unlock)
        pre_unlock_actions_names (str ou list[str,]) , default value = None :
            actions to unlock from the beginning (by default all actions are locked)
        """
        super().__init__(name, potential_actions, pre_unlock_actions_names)

    def get_current_value(self):
        """
        The current value is the number of unlocked actions

        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        return int :
            the current value for this agent = the number of unlocked action
        """
        return len(self._get_unlocked_actions())

    def _get_unlocked_actions(self):
        """
        Get a list of all the unlocked actions of this Agent

        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        return list[AbstractBaseAction] :
            the list of all the unlocked actions

        """
        unlocked_actions = []

        for action in self.potential_actions:
            if action.is_unlock():
                unlocked_actions.append(action)

        return unlocked_actions

    def get_unlocked_actions_names(self):
        return [action.action_name for action in self._get_unlocked_actions()]

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return (
            "\n agent name : "
            + str(self.name)
            + "\n potential_actions are : "
            + str(self.get_all_actions_names())
            + "\n unlocked actions are : "
            + str(self.get_all_unlocked_actions_names())
        )
