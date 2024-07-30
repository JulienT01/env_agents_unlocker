# code coverage : 

[![codecov](https://codecov.io/github/JulienT01/env_agents_unlocker/graph/badge.svg?token=V1UWCV2E38)](https://codecov.io/github/JulienT01/env_agents_unlocker)



# env_agents_unlocker


pour développer l'environmenet:
https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/
https://gymnasium.farama.org/api/env/



Penser à rendre les settings personnalisable au maximum.



1 - Agent principal (qui interéagit avec l'enviroment) : 
    - actions : Peut faire des actions (step) qui unlock les actions des agents de l'environnement.
    - rewards : Dépendent de ce que réussissent à faire les agents de l'environement (somme des rewards indiv des agents secondaires)

2 - Environnement :
    - liste d'agents "secondaires"
    - selon les steps peut libérer les actions "x"
    - Réfléchir sur les observations qu'il retourne
    - 



3 - Agents secondaires (qui vivent dans l'environnement):
    - une liste d'actions potentielles
    - une liste d'action débloquées
    - une fonction objectif qu'il cherche a maximiser selon les actions disponible qu'il a: 
        - le nombre d'action disponnible ?
        - chaque action à une durée et une valeur, et le but est de maximiser les valeurs sur un certains temps donné

4 - Action des agents :
    - option "bloquée"/"débloquée"
    - option "pré-requis" (pour que l'action soit réeelement débloqué il faut aussi que les pré-requis le soient)
    - durée et valeur de l'action  (selon l'agent, elle ne sont pas forcément identiques... tout le monde ne prend pas autant de temps et apporte autant de valeur à chaque action)




