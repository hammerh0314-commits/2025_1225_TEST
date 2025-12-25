import random

# 生成一個隨機數字，範圍1到100
number = random.randint(1, 100)

print("歡迎來到猜數字遊戲！")
print("我已經想好一個1到100的數字，請猜猜看。")

attempts = 0

while True:
    try:
        guess = int(input("請輸入你的猜測："))
        attempts += 1
        
        if guess < number:
            print("太小了！再試試。")
        elif guess > number:
            print("太大了！再試試。")
        else:
            print(f"恭喜你猜對了！答案是 {number}。")
            print(f"你總共猜了 {attempts} 次。")
            break
    except ValueError:
        print("請輸入一個有效的數字。")
    except EOFError:
        print("輸入結束。遊戲退出。")
        break

print("遊戲結束。")