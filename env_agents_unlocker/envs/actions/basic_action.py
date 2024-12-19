from env_agents_unlocker.envs.actions.abstract_action import AbstractBaseAction


class BasicAction(AbstractBaseAction):
    def __init__(
        self, action_name: str, unlocked: bool = False, value: float = None
    ) -> None:
        """
        Basic Action : nothing specific just the simplest implementation of the AbstractBaseAction.
        ------------ Parameters ------------
        action_name (str):
            The name of the action (could be use as ID)
        unlocked (bool) , default value = False :
            The action is unlock for the agent or not
        value (float) , default value = None :
            The value of this action
        """
        super().__init__(action_name, unlocked, value)

    def __eq__(self, other_action) -> bool:
        return (
            isinstance(other_action, BasicAction)
            and self.action_name == other_action.action_name
            and self.unlocked == other_action.unlocked
            and self.value == other_action.value
        )

    def __hash__(self):
        return hash(self.action_name)

    def __str__(self):
        return (
            "\n action name : "
            + str(self.action_name)
            + "\n is unlocked : "
            + str(self.unlocked)
            + "\n value : "
            + str(self.value)
        )
