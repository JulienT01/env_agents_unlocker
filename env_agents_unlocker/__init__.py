from gymnasium.envs.registration import register

register(
    id="env_agents_unlocker/Agent_unlocker-v0",
    entry_point="env_agents_unlocker.envs:AgentUnlockerEnv",
)
