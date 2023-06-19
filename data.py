N_STATES = 16   # 状态数
ACTIONS = ['up','down','left', 'right']     # 动作空间，有4个可以选择的动作
EPSILON = 0.9   # ε-greedy中的ε，数值越小，随机性越强
ALPHA = 0.1     # 学习率
GAMMA = 0.05    # 衰减因子，对于未来的Reward的关注程度
MAX_EPISODES = 100   # 最大episode数

errorStateList=[9,10,11]     #障碍
pathStateList = [1,2,3,4,5,6,7,8,12,13,14,15]      # 路径位置

FRESH_TIME = 0.000    # 时间间隔