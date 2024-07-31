from unittest import TestCase
import gymnasium as gym

from env_agents_unlocker.envs.strategy_creation_env_agents.basic_strategy import (
    BasicStrategyCEA,
)


SETUP_NUMBER_ACTION_AVAILABLE_IN_ENV = 40
SETUP_NUMBER_ACTION_TO_SELECT_BY_AGENT = 20
SETUP_NUMBER_AGENT_TO_CREATE = 200

SETUP_ENV_MAX_STEP = 15


class AgentUnlockerEnv(TestCase):
    def setUp(self):
        env_agents_kwargs = {
            "number_of_agents": SETUP_NUMBER_AGENT_TO_CREATE,
            "nb_available_action_in_env": SETUP_NUMBER_ACTION_AVAILABLE_IN_ENV,
            "nb_action_to_select_by_agent": SETUP_NUMBER_ACTION_TO_SELECT_BY_AGENT,
        }
        strategy = BasicStrategyCEA(
            agents_kwargs=env_agents_kwargs, name="basic_strategy"
        )
        env_kwargs = {
            "strategy_creation_env_agents": strategy,
            "env_max_steps": SETUP_ENV_MAX_STEP,
        }

        self.env = gym.make(
            "env_agents_unlocker:env_agents_unlocker/Agent_unlocker-v0", **env_kwargs
        )

    def test_env_creation(self):
        # check the "setUp" env creation

        assert isinstance(self.env, gym.Env)
        assert self.env.action_space.n == SETUP_NUMBER_ACTION_AVAILABLE_IN_ENV
        assert len(self.env.unwrapped.env_agents) == SETUP_NUMBER_AGENT_TO_CREATE
        assert (
            len(self.env.unwrapped.env_agents[0].get_all_actions_names())
            == SETUP_NUMBER_ACTION_TO_SELECT_BY_AGENT
        )

        self.env.reset()
        step_before_reset = 0
        done = False
        while not done:
            action = self.env.action_space.sample()
            observation, reward, terminated, truncated, info = self.env.step(action)
            step_before_reset += 1
            done = terminated or truncated

        assert step_before_reset == SETUP_ENV_MAX_STEP

    def test_env_step(self):
        self.env.reset()
        assert (
            self.env.unwrapped.env_agents[0].get_current_value() == 0
        )  # basic_agent get 1 point per unlocked action: so 0 after a reset

        action_name_to_unlock = self.env.unwrapped.env_agents[
            0
        ].get_all_actions_names()[
            0
        ]  # get the first action of the first agent to unlock
        assert (
            action_name_to_unlock
            not in self.env.unwrapped.env_agents[0]._get_unlocked_actions()
        )

        action_id = self.env.unwrapped.get_action_id_from_name(action_name_to_unlock)
        self.env.step(action_id)

        assert (
            action_name_to_unlock
            in self.env.unwrapped.env_agents[0].get_unlocked_actions_names()
        )
        assert self.env.unwrapped.env_agents[0].get_current_value() == 1

    def test_env_reset(self):
        self.env.reset()

        action_name_to_unlock = self.env.unwrapped.env_agents[
            0
        ].get_all_actions_names()[
            0
        ]  # get the first action of the first agent to unlock
        action_id = self.env.unwrapped.get_action_id_from_name(action_name_to_unlock)
        self.env.step(action_id)

        # check that 1 action was unlock
        assert (
            action_name_to_unlock
            in self.env.unwrapped.env_agents[0].get_unlocked_actions_names()
        )
        assert self.env.unwrapped.env_agents[0].get_current_value() == 1

        self.env.reset()

        assert len(self.env.unwrapped.env_agents[0].get_unlocked_actions_names()) == 0
        assert self.env.unwrapped.env_agents[0].get_current_value() == 0
