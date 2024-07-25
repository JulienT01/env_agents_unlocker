from abc import ABC, abstractmethod


class AbstractBaseAction(ABC):
    """
    Base class for all Action available for the Agent.
    The other Action should inherite from this class
    """

    def __init__(
        self, action_name: str, unlocked: bool = False, value: float = None
    ) -> None:
        """
        ------------ Parameters ------------
        action_name (str):
            The name of the action (could be use as ID)
        unlocked (bool) , default value = False :
            The action is unlock for the agent or not
        value (float) , default value = None :
            The reward of this action
        """
        self.action_name = action_name
        self.unlocked = unlocked
        self.value = value

    def unlock(self) -> bool:
        """
        Unlock the current action

        ------------ Returns ---------------
        return bool :
            - True if the action was previously locked
            - False if the action was already unlocked
        """
        if not self.unlocked:
            self.unlocked = True
            return True
        else:
            return False

    def get_name(self):
        return self.action_name

    def get_value(self):
        return self.value

    def is_unlock(self):
        return self.unlocked

    @abstractmethod
    def __eq__(self, value: object) -> bool:
        pass

    def to_dict(self):
        """
        Return a dict that describe the current action.
        """
        dict_to_return = {
            "name": self.action_name,
            "unlock": self.unlocked,
            "value": self.value,
        }
        return dict_to_return

    @abstractmethod
    def __hash__(self):
        pass
