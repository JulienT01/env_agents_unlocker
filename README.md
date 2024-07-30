# Badges :

[![codecov](https://codecov.io/github/JulienT01/env_agents_unlocker/graph/badge.svg?token=V1UWCV2E38)](https://codecov.io/github/JulienT01/env_agents_unlocker)



# ENV AGENT UNLOCKER

1 - Agent principal (ce qu'on test, et qui interéagit avec l'enviroment) :
    - actions : Peut prendre des actions (step) qui unlock les actions des agents internes (env_agents) à l'environnement.
    - rewards : Dépend de ce que réussissent à faire les agents internes (env_agents) à l'environement (la somme des rewards indiv des agents secondaires)

2 - Environnement :
    - Possède une liste d'agents "internes" qui rapportent des rewards.
    - Selon les steps pris sur l'environnement, ca peut libérer des actions pour les agents qui y sont.

3 - Agents internes (env_agents) qui sont dans l'environnement:
    - liste d'actions potentielles (débloquées ou non)
    - Liste d'action débloquées
    - une fonction "get_current_reward" que l'agent principal cherche a maximiser (en débloquant les actions disponibles des agents internes) :
        - le nombre d'agent débloqué ?
        - chaque action à une valeur (qui peut être différente ou non entre les agents internes):
            - la valeur de l'action débloqué qui à la valeur max
            - la somme des valeurs des actions débloquées


4 - Actions des agents :
    - option "bloquée"/"débloquée"









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
        -pré-requis étant d'autres agents
        - d'autres pré-requis ?
    - durée et valeur de l'action  (selon l'agent, elle ne sont pas forcément identiques... tout les agents ne prennent pas autant de temps et accorde autant de valeurs à chaque action)
