import gymnasium as gym
import numpy as np
from gymnasium import spaces
from env_agents_unlocker.envs.strategy_creation_env_agents import (
    abstract_strategy_creation_env_agents,
)

# import pygame

############ TODO ###########

# ajouter le type_of_agent et le number_of_agent_to_create  dans le "agents_kwargs" ???
#############################


class AgentUnlockerEnv(gym.Env):
    # metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(
        self,
        strategy_creation_env_agents: abstract_strategy_creation_env_agents,
        env_max_steps=None,
        render_mode=None,
    ):
        """
        ------------ Parameters ------------
        strategy_creation_env_agents (dict) :
            The strategy to create and manage the list of Agents living in the environment.
        env_max_steps (int) :
            The number of step before terminating the env
        """
        self.strategy_creation_env_agents = strategy_creation_env_agents
        self.env_max_steps = env_max_steps
        self.current_nb_steps = 0
        self.env_agents = []  # will be initialized in _init_agents()
        self.action_list = []  # will be initialized in _init_agents()
        self.action_space = None  # will be initialized in _init_agents()
        # map of the abstract actions from `self.action_space` to the action to unlock
        self._action_id_to_action_name = {}
        self._action_name_to_action_id = {}

        self._init_agents()

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def _init_agents(self):
        self.env_agents = self.strategy_creation_env_agents.create_new_agent_list()

        # get the list of existing action
        temp_action_list = []
        for agent in self.env_agents:
            temp_action_list += agent.get_all_actions_names()
        # make all actions unique
        self.action_list = list(set(temp_action_list))

        self.action_space = spaces.Discrete(len(self.action_list))
        self.observation_space = spaces.Dict(
            {
                "agents": spaces.Sequence(
                    spaces.Dict(
                        {
                            "name": spaces.Text(250),
                            "all_actions": spaces.Sequence(
                                spaces.Dict(
                                    {
                                        "name": spaces.Text(250),
                                        "unlock": spaces.Box(0, 1),
                                        "value": spaces.Box(-100000, +100000),
                                    }
                                )
                            ),
                            "unlocked_action": spaces.Sequence(
                                spaces.Dict(
                                    {
                                        "name": spaces.Text(250),
                                        "unlock": spaces.Box(0, 1),
                                        "value": spaces.Box(-100000, +100000),
                                    }
                                )
                            ),
                        }
                    )
                ),
            }
        )

        # maps abstract actions from `self.action_space` to the action to unlock
        for id, name in enumerate(self.action_list):
            self._action_id_to_action_name[id] = name
            self._action_name_to_action_id[name] = id

        self.current_nb_steps = 0

    def _get_obs(self):
        return self.strategy_creation_env_agents.get_obs()

    def _get_final_info(self):
        return self.strategy_creation_env_agents.get_final_results()

    def _get_current_info(self):
        return self.strategy_creation_env_agents.get_current_info()

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self._init_agents()

        observation = self._get_obs()
        info = self._get_current_info()

        # if self.render_mode == "human":
        #     self._render_frame()

        return observation, info

    def get_action_id_from_name(self, action_name):
        return self._action_name_to_action_id[action_name]

    # def get_action_name_from_id(self, action_id):
    #     return self._action_id_to_action_name[action_id]

    def step(self, actions_id):
        """
        action_id can be a int or a list(int)
        """
        previous_env_value = (
            self.strategy_creation_env_agents.compute_env_current_value()
        )

        actions_to_unlock = []
        if isinstance(actions_id, (int, np.integer)):
            actions_to_unlock = self._action_id_to_action_name[actions_id]
        elif isinstance(actions_id, list):
            for act_id in actions_id:
                actions_to_unlock.append(self._action_id_to_action_name[act_id])
        else:
            error_message = "The step parameter should be a int or a list(int)"
            print(error_message)
            raise TypeError(error_message)

        for agent in self.env_agents:
            agent.unlock_actions(actions_to_unlock)

        self.current_nb_steps += 1

        new_env_value = self.strategy_creation_env_agents.compute_env_current_value()

        # An episode is done if the current number of steps is superior to the env_max_steps value
        terminated = True if (self.current_nb_steps >= self.env_max_steps) else False
        reward = new_env_value - previous_env_value
        observation = self._get_obs()
        info = self._get_final_info() if terminated else self._get_current_info()

        # if self.render_mode == "human":
        #     self._render_frame()

        return observation, reward, terminated, False, info

    # def render(self):
    #     if self.render_mode == "rgb_array":
    #         return self._render_frame()

    # def _render_frame(self):
    #     if self.window is None and self.render_mode == "human":
    #         pygame.init()
    #         pygame.display.init()
    #         self.window = pygame.display.set_mode((self.window_size, self.window_size))
    #     if self.clock is None and self.render_mode == "human":
    #         self.clock = pygame.time.Clock()

    #     canvas = pygame.Surface((self.window_size, self.window_size))
    #     canvas.fill((255, 255, 255))
    #     pix_square_size = (
    #         self.window_size / self.size
    #     )  # The size of a single grid square in pixels

    #     # First we draw the target
    #     pygame.draw.rect(
    #         canvas,
    #         (255, 0, 0),
    #         pygame.Rect(
    #             pix_square_size * self._target_location,
    #             (pix_square_size, pix_square_size),
    #         ),
    #     )
    #     # Now we draw the agent
    #     pygame.draw.circle(
    #         canvas,
    #         (0, 0, 255),
    #         (self._agent_location + 0.5) * pix_square_size,
    #         pix_square_size / 3,
    #     )

    #     # Finally, add some gridlines
    #     for x in range(self.size + 1):
    #         pygame.draw.line(
    #             canvas,
    #             0,
    #             (0, pix_square_size * x),
    #             (self.window_size, pix_square_size * x),
    #             width=3,
    #         )
    #         pygame.draw.line(
    #             canvas,
    #             0,
    #             (pix_square_size * x, 0),
    #             (pix_square_size * x, self.window_size),
    #             width=3,
    #         )

    #     if self.render_mode == "human":
    #         # The following line copies our drawings from `canvas` to the visible window
    #         self.window.blit(canvas, canvas.get_rect())
    #         pygame.event.pump()
    #         pygame.display.update()

    #         # We need to ensure that human-rendering occurs at the predefined framerate.
    #         # The following line will automatically add a delay to keep the framerate stable.
    #         self.clock.tick(self.metadata["render_fps"])
    #     else:  # rgb_array
    #         return np.transpose(
    #             np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
    #         )

    # def close(self):
    #     if self.window is not None:
    #         pygame.display.quit()
    #         pygame.quit()
