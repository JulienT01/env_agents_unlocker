from abc import ABC, abstractmethod

from env_agents_unlocker.envs.env_agents.abstract_base_agent import AbstractBaseAgent


####### TODO? #######

# faire une fonction print_kwargs_structure(type_of_agents) pour afficher sous quelle forme devrait être le agents_kwargs
# faire un objet qui prend en paramètre une fonction et les paramètre de cette fonction... pour que les gens puissent donner exactement ce qu'ils veulent, plutot que d'écrire du code ici
# voir tout passer en parametre (la classe Agent, la classe Action, la stratégie sous forme d'une fonction)
#####################


class AbstractStrategyCreationEnvAgents(ABC):
    """
    Base class for all Agents living in the environment.
    The other agent should inherit from this class
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        ------------ Parameters ------------
        name (str):
            The name of the strategy
        """
        self.name = name

    @abstractmethod
    def create_list_of_agents(agents_kwargs: dict) -> list[AbstractBaseAgent]:
        """
            Main function in charge to give the expected list of Agent(inherited from AbstractBaseAgent)

        ------------ Parameters ------------
        agents_kwargs (dict) :
            parameters specific to create these agents (and actions for theses agent)

        ------------ Returns ---------------
        list(AbstractBaseAgent) :
        list(AbstractBaseAgent) list of agents in the environment

        """

    @abstractmethod
    def __hash__(self):
        """abstract method"""

    @abstractmethod
    def __eq__(self):
        """abstract method"""

    @abstractmethod
    def __str__(self):
        """abstract method"""
