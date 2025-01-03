from abc import ABC, abstractmethod

from env_agents_unlocker.envs.actions.basic_action import AbstractBaseAction


####### TODO? #######

# - une liste d'actions potentielles
# - une liste d'action débloquées
# - une fonction objectif qu'il cherche a maximiser selon les actions disponible qu'il a:
#     - le nombre d'action disponnible ?
#     - chaque action à une durée et une valeur, et le but est de maximiser les valeurs sur un certains temps donné


#####################


class AbstractBaseAgent(ABC):
    """
    Base class for all Agents living in the environment.
    The other agent should inherit from this class
    """

    def __init__(
        self,
        name: str,
        potential_actions: list[AbstractBaseAction],
        pre_unlock_actions_names: list[str] = None,
    ) -> None:
        """
        ------------ Parameters ------------
        name (str):
            The name of the agent (could be use as ID)
        potential_actions (list[AbstractBaseAction]):
            List of all the actions for this agent (lock and unlock)
        pre_unlock_actions_names (str ou list[str,]) , default value = None :
            actions to unlock from the beginning (by default all actions are locked)
        """
        self.name = name
        self.potential_actions = potential_actions

        if pre_unlock_actions_names is not None:
            self.unlock_actions(pre_unlock_actions_names)

    def unlock_actions(self, actions_to_unlock):
        """
        Correspond to the "step" from  gymnasium env.
        Function that unlock a specific list of action for the current Agent

        Warning : there is no feedback about the previous state of the action, or even if the action exist for this agent.
        The function can be overwrite if you need a specific functionality.

        ------------ Parameters ------------
        actions_to_unlock (str ou list[str,]) :
            actions to unlock

        ------------ Returns ---------------
        None

        """
        if isinstance(actions_to_unlock, str):
            actions_to_unlock = [actions_to_unlock]

        for action in self.potential_actions:
            if action.get_name() in actions_to_unlock:
                action.unlock()

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

    def get_all_actions_names(self):
        return [action.get_name() for action in self.potential_actions]

    def get_all_unlocked_actions_names(self):
        return [action.get_name() for action in self._get_unlocked_actions()]

    @abstractmethod
    def get_current_value(self):
        """
        Abstract method : return a score on "how the agent did with the current unlocked actions"
        """

    def to_dict(self):
        """
        Return a dict that describe the current agent.
        """
        dict_to_return = {
            "name": self.name,
            "all_actions": list(map(lambda x: x.to_dict(), self.potential_actions)),
            "unlocked_action": list(
                map(lambda x: x.to_dict(), self._get_unlocked_actions())
            ),
        }
        return dict_to_return

    @abstractmethod
    def __hash__(self):
        """abstract method"""

    @abstractmethod
    def __str__(self):
        """abstract method"""
