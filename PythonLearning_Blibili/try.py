import time

print("警告！警告！系统检测到异常活动！")
print("请立即输入'黄宸毅最帅'以解除警报。")

while True:
    user_input = input("请输入：")
    if user_input == "我是最棒的":
        print("警报解除。系统恢复正常。")
        break
    else:
        print("警告！系统即将重启！")
        time.sleep(2)  # 暂停2秒
        print("警告！系统即将关闭！")
        time.sleep(2)
        print("警告！系统即将格式化硬盘！")
        time.sleep(2)
        print("警告！系统即将自毁！")
        time.sleep(2)
        print("警报解除。系统恢复正常。")
        time.sleep(1)