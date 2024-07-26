from env_agents_unlocker.envs.secondary_agents.basic_agent import BasicAgent
from env_agents_unlocker.envs.secondary_agents.basic_agent import AbstractBaseAgent
from env_agents_unlocker.envs.actions.basic_action import BasicAction

import random

####### TODO? #######

# faire une fonction print_kwargs_structure(type_of_agents) pour afficher sous quelle forme devrait être le agents_kwargs
# faire un objet qui prend en paramètre une fonction et les paramètre de cette fonction... pour que les gens puissent donner exactement ce qu'ils veulent, plutot que d'écrire du code ici
# voir tout passer en parametre (la classe Agent, la classe Action, la stratégie sous forme d'une fonction)
#####################


def create_list_of_agents(
    number_of_agent_to_create: int, type_of_agents: str, agents_kwargs: dict
) -> list[AbstractBaseAgent]:
    """
        Main function in charge to give the expected list of Agent(inherited from AbstractBaseAgent)

    ------------ Parameters ------------
    number_of_agent_to_create (int) :
        the number of Agent in the returned list
    type_of_agents :
        what kind of agents should it be (agents's creation startegy)
    agents_kwargs (dict) :
        settings specific to these agents to create (and actions for theses agent)

    ------------ Returns ---------------
    list(AbstractBaseAgent) :
      list(AbstractBaseAgent) where each of them have the same list(BasicAction)

    """
    agent_list_to_return = []

    if type_of_agents == "all_basic":
        agent_list_to_return = _get_new_all_basic_agents(
            number_of_agent_to_create, agents_kwargs
        )
    else:
        raise NotImplementedError(
            "Unknown 'type_of_agents' for the 'create_list_of_agents' function."
        )

    return agent_list_to_return


def _get_new_all_basic_agents(
    number_of_agent_to_create: int, agents_kwargs: dict
) -> list[AbstractBaseAgent]:
    """
    Get a list of basic agents that all have the same kind of basic (locked) actions.
    It's will be a list of BasicAgent, where each of them have a list of BasicAction  (subpart of all the same BasicAction available).

    ------------ Parameters ------------
    number_of_agent_to_create (int) :
        the number of BasicAgent in the returned list
    agents_kwargs (dict) :
        settings specific to the agents (and actions for this agent) to create. Here (key):
            - nb_available_action_in_env : the size of all available actions
            - nb_action_to_select_by_agent : the size of action list for each agent

    ------------ Returns ---------------
    list(BasicAgent) :
      list(BasicAgent) where each of them have the same list(BasicAction)

    """
    basic_agent_list = []

    nb_available_action_in_env = agents_kwargs["nb_available_action_in_env"]
    available_actions = []
    for j in range(nb_available_action_in_env):
        available_actions.append(
            BasicAction(action_name=str(j), unlocked=False, value=1)
        )

    for i in range(number_of_agent_to_create):
        nb_action_to_select_by_agent = agents_kwargs["nb_action_to_select_by_agent"]
        actions_for_this_agent = random.sample(
            available_actions, nb_action_to_select_by_agent
        )

        basic_agent_list.append(
            BasicAgent(
                name=str(i),
                potential_actions=actions_for_this_agent,
                pre_unlock_actions=None,
            )
        )
    return basic_agent_list
