from abc import ABC, abstractmethod

from env_agents_unlocker.envs.env_agents.abstract_base_agent import AbstractBaseAgent


####### TODO? #######

# faire une fonction print_kwargs_structure(type_of_agents) pour afficher sous quelle forme devrait être le agents_kwargs
# faire un objet qui prend en paramètre une fonction et les paramètre de cette fonction... pour que les gens puissent donner exactement ce qu'ils veulent, plutot que d'écrire du code ici
# voir tout passer en parametre (la classe Agent, la classe Action, la stratégie sous forme d'une fonction)
#####################


class AbstractStrategyCreationEnvAgents(ABC):
    """
    Base class for all Strategy to manage the creation of Agent living in the environment.
    The created strategies should inherit from this class
    """

    def __init__(
        self,
        agents_kwargs: dict,
        name: str,
    ) -> None:
        """
        ------------ Parameters ------------
        name (str):
            The name of the strategy
        agents_kwargs (dict) :
            parameters specific to create these agents (and actions for theses agent)
        """
        self.agents_kwargs = agents_kwargs
        self.name = name

    @abstractmethod
    def _create_list_of_agents(self) -> list[AbstractBaseAgent]:
        """
            Function in charge to create the expected list of Agent(inherited from AbstractBaseAgent)

        ------------ Parameters ------------

        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment
        """

    @abstractmethod
    def get_list_of_agents(self) -> list[AbstractBaseAgent]:
        """
            Get the list of agent created by the strategy
        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment
        """

    @abstractmethod
    def create_new_agent_list(self) -> list[AbstractBaseAgent]:
        """
        Replace the previous list, by a new one (to call on the reset)
        ------------ Parameters ------------
        None

        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment
        """

    @abstractmethod
    def compute_env_current_value(self):
        """abstract method : how to compute the value of the environment (current state)."""

    @abstractmethod
    def get_obs(self):
        """abstract method : what should be return as 'observation' of the environment (current state)."""

    @abstractmethod
    def get_final_results(self):
        """abstract method : what should be return as 'final state' of the environment (will be in the 'info' return, when the state is 'terminated')."""

    @abstractmethod
    def __hash__(self):
        """abstract method"""

    @abstractmethod
    def __eq__(self):
        """abstract method"""

    @abstractmethod
    def __str__(self):
        """abstract method"""
