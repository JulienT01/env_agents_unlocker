from env_agents_unlocker.envs.env_agents.abstract_base_agent import (
    AbstractBaseAgent,
)
from env_agents_unlocker.envs.actions.basic_action import AbstractBaseAction


class BasicAgentWithMaxValue(AbstractBaseAgent):
    def __init__(
        self,
        name: str,
        potential_actions: list[AbstractBaseAction],
        pre_unlock_actions_names: list[str] = None,
    ) -> None:
        """
        Basic Agent, its objective (to maximize its value) is to unlock the action with the max value. (action with the max value only, other actions are useless)
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
        The current value is the best value of the unlocked actions

        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        return int :
            best value of the unlocked actions
        """
        return self._get_best_current_unlocked_value()

    def _get_best_current_unlocked_value(self):
        best_value = None
        for action in self._get_unlocked_actions():
            current_action_value = action.value
            if best_value is None or best_value < current_action_value:
                best_value = current_action_value
        return best_value

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
            + "\n best current value is : "
            + str(self._get_best_current_unlocked_value())
        )
