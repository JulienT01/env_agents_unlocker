from env_agents_unlocker.env.secondary_agents.abstract_base_agent import (
    AbstractBaseAgent,
)
from env_agents_unlocker.env.actions.basic_action import AbstractBaseAction


class BasicAgent(AbstractBaseAgent):
    def __init__(
        self,
        name: str,
        potential_actions: list[AbstractBaseAction],
        pre_unlock_actions: list[str] = None,
    ) -> None:
        """
        Basic Agent, its objective (to maximize its reward) is to unlock the maximum of its actions
        ------------ Parameters ------------
        name (str):
            The name of the agent (could be use as ID)
        potential_actions (list[AbstractBaseAction]):
            List of all the actions for this agent (lock and unlock)
        pre_unlock_actions (str ou list[str,]) , default value = None :
            actions to unlock from the begining (by default all actions are locked)
        """
        super().__init__(name, potential_actions, pre_unlock_actions)

    def get_current_reward(self):
        """
        The current reward is the number of unlocked actions

        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        return int :
            the current reward for this agent
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
        unlocked_action = []

        for action in self.potential_actions:
            if action.is_unlock():
                unlocked_action.append(action)

        return unlocked_action

    def to_dict(self):
        dict_to_return = {
            "name": self.name,
            "all_actions": list(map(lambda x: x.to_dict(), self.potential_actions)),
            "unlocked_action": list(
                map(lambda x: x.to_dict(), self._get_unlocked_actions())
            ),
        }
        return dict_to_return
