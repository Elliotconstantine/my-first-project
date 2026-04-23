import random
secret_number = random.randint(1, 100)
guess = 0
print("欢迎来到猜数字游戏！我想了一个1到100之间的数字。")
while guess != secret_number:
    guess = int(input("请输入你的猜测："))
    if guess < secret_number:
        print("太小了！再试一次。")
    elif guess > secret_number:
        print("太大了！再试一次。")
    else:
        print("恭喜你！猜对了！")
# 这是一个简单的猜数字游戏，玩家需要猜测一个1到100之间的随机数。程序会提示玩家猜测的数字是太大了还是太小了，直到玩家猜对为止。
