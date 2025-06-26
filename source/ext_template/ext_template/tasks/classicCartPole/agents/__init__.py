import gymnasium as gym

from ext_template.tasks.classicCartPole.robot import cartpole_env_cfg 

##
# Register Gym environments.
##

gym.register(
    id="Template-Isaac-CartPole-PPO-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": cartpole_env_cfg.CartpoleEnvCfg,
        "rsl_rl_cfg_entry_point": f"{__name__}.rsl_rl_ppo_cfg:CartPolePPORunnerCfg",
    },
)