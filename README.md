# Badges :

[![codecov](https://codecov.io/github/JulienT01/env_agents_unlocker/graph/badge.svg?token=V1UWCV2E38)](https://codecov.io/github/JulienT01/env_agents_unlocker)



# ENV AGENT UNLOCKER

Environnement basé sur l'API gymnasium (step/reset/reward/observation/...).
Quelques spécificités :
- pour l'instant il n'y a pas de rendering
- selon la stratégie, on peut renvoyer des informations différentes entre l'"observation" de chaque step, et le resultat final : lorsque l'environement passe en état "terminated", vous pouvez trouver l'état final de l'environnement dans le dictionnaire "info".




1 - Agent principal (ce qu'on test, et qui interéagit avec l'enviroment) :
    - actions : Peut prendre des actions (step) qui unlock les actions des agents internes (env_agents) à l'environnement.
    - rewards : Dépend de ce que réussissent à faire les agents internes (env_agents) à l'environement (la somme des rewards indiv des agents internes)

2 - Environnement :
    - Possède une liste d'agents "internes" qui ont des rewards individuellement.
    - Selon les steps pris par l'agent principal sur l'environnement, ca peut libérer des actions pour les agents internes qui y sont.

3 - Agents internes (env_agents) qui sont dans l'environnement:
    - liste d'actions potentielles (débloquées ou non)
    - Liste d'action débloquées
    - une fonction "get_current_value" que l'agent principal cherche a maximiser (en débloquant les actions disponibles pour les agents internes) :
        - le nombre d'agent débloqué ?
        - chaque action à une valeur (qui peut être différente ou non entre les agents internes):
            - la valeur de l'action débloqué qui à la valeur max
            - la somme des valeurs des actions débloquées

4 - Actions des agents :
    - option "bloquée"/"débloquée"







## Actions
### Basic action
Action classique : juste un nom, une valeur, et bloquée/débloquée.

## Env agents
### Basic agent
La valeur renvoyé par ces agents correspond aux nombres d'actions qu'ils ont débloqué (peu importe la valeur de ces actions).

### Basic agent with max value
La valeur renvoyé par ces agents correspond à la valeur de l'action débloquée qui à la plus haute valeur.

### Basic agent with cumulative value
La valeur renvoyé par ces agents correspond à la somme de toutes les valeurs des actions débloquées.

## Stratégies
### Basic strategy

liste des kwargs :
    - nb_available_action_in_env (int): the size of all available actions
    - nb_action_to_select_by_agent (int): the size of action list for each agent
    - number_of_agents (int): the number of Agent

Il s'agit de la stratégie la plus simple.
On a un certains nombre d'actions (Basic action) possible dans l'environement.
Chaque agent (Basic agent) à un nombre fixe d'actions tirées au hasard dans les actions de l'environnment

La valeur de l'environnement correspond à la somme des valeurs des agents (Basic agent)

### Same actions different values

liste des kwargs :
    - number_of_agents (int) : the number of Agent in the returned list
    - nb_action_by_agent (int): the size of action list for each agent
    - agent_class (subclass of AbstractBaseAgent): class of expected agent to instantiate

Il s'agit d'une stratégie ou tous les agents ont les mêmes actions, mais ces actions ont des valeurs différentes selon les agents.
Le type d'agent est passé en paramètre, ce qui peut permetre (entre autre) d'utiliser les "Basic agent with max value" ou "Basic agent with cumulative value".   (Le 'basic agent' n'est pas utile puisqu'il ne prend pas en compte les valeurs des actions)

La valeur de l'environnement correspond à la somme des valeurs des agents (Basic agent)

### Same actions different values with negative values

liste des kwargs :
    - number_of_agents (int) : the number of Agent in the returned list
    - nb_positive_action_by_agent (int): the number of action with positive value for each agent
    - nb_negative_action_by_agent (int): the number of action with negative value for each agent
    - agent_class (subclass of AbstractBaseAgent): class of expected agent to instantiate

Tous les agents ont le même nombre d'action, mais ces actions ont différentes valeurs selon les agents.
Ces valeurs peuvent également être négative. Le nombre d'action à valeur positive et négative doit être spécifier via les kwargs

Pour bénéficier de la difficultés de débloquer uniquement les agents avec des valeurs positives, il est recommandé d'utiliser des "Basic agent with cumulative value".

La valeur de l'environnement correspond à la somme des valeurs des agents (Basic agent)

# TODO

pour développer l'environmenet:
https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/
https://gymnasium.farama.org/api/env/



Penser à rendre les settings personnalisable au maximum.



1 - Agent principal (qui interéagit avec l'enviroment) :
    - done so far

2 - Environnement :
    - Réfléchir sur les observations qu'ils retournent


3 - Agents secondaires (qui vivent dans l'environnement):
    - ajouter des durées aux actions (pendant 1 step, un agent pourrait faire plusieurs actions basée sur une "durée max par step", et ou chaque action prends une certaine durée)
        - chaque action à une durée et une valeur, et le but est de maximiser les valeurs sur un certains temps donné

4 - Actions des agents :
    - ajouté une option de "pré-requis" (pour que l'action soit réeelement débloqué il faut aussi que les pré-requis le soient)
        -pré-requis étant d'autres actions  (mais doit être géré par les agents eux-mêmes)
        - d'autres pré-requis ?
        - comment construire automatiquement un "arbre" d'actions avec pré-requis
        - faire des pré-requis négatifs (si une certaine action est débloquée, l'autre n'est plus déblocable (voir se rebloque?))

    - durée et valeur de l'action  (selon l'agent, elle ne sont pas forcément identiques... tout les agents ne prennent pas autant de temps et accorde autant de valeurs à chaque action)

5 - faire des stratégies adverserials :
    - avec des actions qui ont des valeurs négative
    - avec des agents qui ont plus de "bonnes actions" et d'autres agents qui ont plus de "mauvaise action"
    - avec des actions/ ou agents qui ont des meilleurs actions
    - value de l'environement n'est pas directement liée à la valeur des agents qui le compose (agentbasic qui ne prend pas en compte la valeur de ses agents)
    - adverserial agent (qui peuvent influer sur les autres agents)
        - Agent qui "trichent" sur la vraie valeur de leurs actions (valeur élevée, mais sabotent les autres agents)
    - stratégie qui cache complétement la value lors de ses observations, mais affiche son résultat à la fin (l'IA doit faire en fonction du nombre d'action débloquée.)
    - beaucoup d'action partagées "mauvaise", et peu de "bonne" action  (trouver lesquels débloquer)
    - Agent capable de se dupliquer?
    - action qui à une valeur qui peut changer dans le temps  (un truc positif, qui après devient négatif)
