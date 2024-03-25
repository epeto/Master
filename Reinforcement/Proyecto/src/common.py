

HYPERPARAMS = {
    'tank': {'env_name': "Tanque_v1",
             'stop_reward': 1,
             'run_name': 'tank',
             'replay_size': 10000,
             'replay_initial': 1000,
             'target_net_sync': 1000,
             'epsilon_frames': 10**5,
             'epsilon_start': 1.0,
             'epsilon_final': 0.02,
             'learning_rate': 0.0001,
             'gamma': 0.99,
             'batch_size': 32}}

