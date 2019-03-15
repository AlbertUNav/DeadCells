from gym.envs.registration import register

register(
    id='deadcells-v0',
    entry_point='gym_deadcells.envs:DeadCellsEnv',
)
register(
    id='deadcells-extrahard-v0',
    entry_point='gym_deadcells.envs:DeadCellsxtraHardEnv',
)
