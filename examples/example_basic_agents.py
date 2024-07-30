import gymnasium as gym
from env_agents_unlocker.envs.strategy_creation_env_agents.basic_strategy import (
    BasicStrategyCEA,
)

my_strategy = BasicStrategyCEA(name="basic_strategy")

env_agents_kwargs = {
    "number_of_agents": 200,
    "nb_available_action_in_env": 40,
    "nb_action_to_select_by_agent": 20,
}

env_kwargs = {
    "strategy_creation_env_agents": my_strategy,
    "strategy_agents_kwargs": env_agents_kwargs,
    "env_max_steps": 15,
}


env = gym.make(
    "env_agents_unlocker:env_agents_unlocker/Agent_unlocker-v0", **env_kwargs
)

env.reset()
# print("reset done : ", result)
run_number = 1
cum_reward = 0
for tt in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    cum_reward += reward
    if done:
        print(
            "run number ",
            run_number,
            ", last reward = ",
            reward,
            " run cumulative reward = ",
            cum_reward,
        )
        env.reset()
        cum_reward = 0
        run_number += 1


# print("action_space : ", env.action_space)

print("done !!!")
