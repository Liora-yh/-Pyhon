# 发工资
# 某公司账户余额有1W元，给20名员工发放工资。
# 员工编号从1到20，编号从1开始，依此领取工资，没人可以领取1000元        # 可以通过循环发放工资
# 领工资时，财务判断员工的绩效分(1-10)（随机生成），如果低于5，不发工资，换下一位     # 通过continue跳过员工
# 如果工资领完了，结束发工资         # 通过break结束循环


money = 10000
for emp_id in range(1, 21):
    import random
    emp_grade = random.randint(1, 10)
    if emp_grade < 5:
        print(f"员工{emp_id}，绩效分{emp_grade}，低于5，不发放工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"向员工{emp_id}发放工资1000元，账户余额{money}")
    else:
        print("工资发完了，下个月领取吧。")
        break
