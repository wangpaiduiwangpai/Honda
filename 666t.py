import random

def myFunc(n, stepper):
    """
    :参数 n: 目标数
    :参数 stepper: 步进范围（可以走几步的最大值）
    :返回值: （flag,first_num,total_stepper）
            第一个出还是第二个出：flag=1,第一个出；flag = 0第二个出
                如果第一个出：第一次出多少 first_num
                如果第二个出：出的数总和为多少 total_stepper
    """
    total_stepper = stepper + 1  # 组合数
    if n % total_stepper == 0:  #能整除的情况
        print("目标数：{}，步进范围：{}，组合数：{}".format(n, stepper, total_stepper))
        flag = 0   # 对方先出
        return (flag, 0, total_stepper)
    else:
        v_num = n - stepper - 1  # 拿到v_num就一定能数到目标数
        if v_num % total_stepper == 0:   # v_num能被组合数整除的情况
            flag = 0    # 对方先出
            print("目标数：{}， 步进范围：{}， 组合数：{}, 是否第一个出：{}".format(n, stepper, total_stepper, flag))
            return (flag, 0, total_stepper)
        else:
            flag = 1   # 我方先出
            first_num = v_num % total_stepper    # 我第一次数的数，这个数将v_num钝化为可以被组合数整除的数
            print("目标数：{}， 步进范围：{}， 组合数：{}, 是否第一个出：{}, 出多少：{}".format(n, stepper, total_stepper, flag, first_num))
            return (flag, first_num, total_stepper)

print(myFunc(1024,4))