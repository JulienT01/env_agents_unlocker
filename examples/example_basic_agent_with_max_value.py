"""
Agent that randomly unlocks actions in an environment that follows SameActionsDifferentValuesStrategyCEA (each agent has the same list of actions to unlock, but the value of these actions are different)
the reward is the sum of "the value of the biggest unlocked action" for each agent
"""

import gymnasium as gym

from env_agents_unlocker.envs.strategy_creation_env_agents.same_actions_different_values import (
    SameActionsDifferentValuesStrategyCEA,
)
from env_agents_unlocker.envs.env_agents.basic_agent_with_max_value import (
    BasicAgentWithMaxValue,
)

env_agents_kwargs = {
    "number_of_agents": 20,
    "nb_action_by_agent": 1000,
    "agent_class": BasicAgentWithMaxValue,
}

my_strategy = SameActionsDifferentValuesStrategyCEA(agents_kwargs=env_agents_kwargs)

env_kwargs = {
    "strategy_creation_env_agents": my_strategy,
    "env_max_steps": 100,
}


env = gym.make(
    "env_agents_unlocker:env_agents_unlocker/Agent_unlocker-v0", **env_kwargs
)

env.reset()
# print("reset done : ", result)
run_number = 1
cum_reward = 0
for tt in range(3000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    cum_reward += reward
    if done:
        print(
            "run number ",
            run_number,
            " : last reward = ",
            reward,
            ", run cumulative reward = ",
            cum_reward,
        )
        env.reset()
        cum_reward = 0
        run_number += 1


# print("action_space : ", env.action_space)

print("done !!!")
