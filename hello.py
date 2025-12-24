print("Hello World")
print("欢迎使用Python计算机！")
while True:
    try:
        expr = input(">>> ")
        if expr.strip().lower() in ("exit", "quit"):
            print("退出计算机。")
            break
        # 安全地只允许计算表达式
        result = eval(expr, {"__builtins__": {}})
        print(result)
    except Exception as e:
        print("错误：", e)
