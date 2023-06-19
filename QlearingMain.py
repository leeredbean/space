import numpy as np
import pandas as pd
import time
import sys

np.random.seed(2)  # 设置随机种子，保证生成随机数相同

from data import *

# 建立Q表函数
def create_Q_table(state, actions):  # 输入状态数和动作空间
    table = pd.DataFrame(np.zeros((state, len(actions))), columns=actions)  # 创建一个表格，大小为状态数*动作数，列名为动作空间名称
    print("创建的Q表如下：")
    print(table)  # 输出Q表
    return table


# 动作选择函数，根据ε和Q值选择状态s下的最佳动作
def choose_action(state, q_table,episode):

    state_actions = q_table.iloc[state, :]  # 选择表格对应s行的所有列值
    #EPSILON=0.5*(1/(episode+1))
    #if (np.random.uniform() >= EPSILON) or (state_actions.all() == 0):  # 生成随机数
        #action_name = np.random.choice(ACTIONS)   # 随机选择一个动作
    #else:
        #action_name = state_actions.idxmax()  # 返回最大Q值对应的动作名称
    #return action_name

    update_flag = False
    for item in state_actions:
        if (item > 0):
            update_flag = True

    if (state_actions.all() == 0):  # 四个动作Q值都为0
        action_name = np.random.choice(ACTIONS)  # 随机选择一个动作，返回动作名称"left" 或 "right" "up" "down"
    elif ((update_flag == False) and (np.random.uniform() > EPSILON)):
        action_name = np.random.choice(ACTIONS)
    elif ((update_flag == True) and (np.random.uniform() > (EPSILON + (1 - EPSILON) * 0.5))):
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.idxmax()  # 返回最大Q值对应的动作名称
    return action_name  # 返回名称，可能因为pandas用列名访问

# 奖励函数
def get_env_feedback(state, action):  # 输入一个状态和动作
    global R
    if action == 'up':
        if state in [0,1,2,3]:
            state = 'over'
            R = -100
        else:
            state = state - 4
            if state in errorStateList:
                state='over'
                R=-10
            elif state in pathStateList:
                R = 10

    if action == 'down':
        if state in [12, 13, 14, 15]:
            state = 'over'
            R = -100
        else:
            state = state + 4

            if state in errorStateList:
                state='over'
                R=-10
            elif state in pathStateList:
                R = 10



    if action == 'left':
        if state in [0, 4, 8, 12]:
            state = 'over'
            R = -100
        else:
            state = state - 1

            if state in errorStateList:
                state='over'
                R=-10
            elif state in pathStateList:
                R = 10

    if action == 'right':
        if state in [3, 7,11, 15]:
            state = 'over'
            R = -100
        else:
            state = state + 1
            if state in errorStateList:
                state='over'
                R=-10
            elif state in pathStateList:
                R = 10


     # 返回下一个状态及奖励
    return state, R