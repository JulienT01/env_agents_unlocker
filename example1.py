import gymnasium as gym


env_agents_kwargs = {
    "nb_available_action_in_env": 40,
    "nb_action_to_select_by_agent": 20,
}

env_kwargs = {
    "number_of_agent_to_create": 200,
    "type_of_agents": "all_basic",
    "agents_kwargs": env_agents_kwargs,
    "env_max_steps": 15,
}


env = gym.make(
    "env_agents_unlocker:env_agents_unlocker/Agent_unlocker-v0", **env_kwargs
)

env.reset()
# print("reset done : ", result)
run_number = 1
for tt in range(300):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

    if done:
        print("run number ", run_number, ", final reward = ", reward)
        env.reset()
        run_number += 1


# print("action_space : ", env.action_space)

print("done !!!")
