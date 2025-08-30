card_number = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
               "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
               "J": 11, "Q": 12, "K": 13}


def verification(calculation_order):
    try:
        result = eval(calculation_order)
    except ZeroDivisionError:
        return None
    return result == 24


def operator_solutions(cards):
    solutions = set()
    nums = []
    for card in cards:
        nums.append(card_number[card])

    # 遍历所有可能的排列组合
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for k in range(4):
                if k == i or k == j:
                    continue
                l = 6 - i - j - k
                correspond_num = [nums[i], nums[j], nums[k], nums[l]]

                # 遍历所有可能的操作符组合
                for op1 in "+-*/":
                    for op2 in "+-*/":
                        for op3 in "+-*/":
                            calculation_orders = [
                                f"(({correspond_num[0]}{op1}{correspond_num[1]}){op2}{correspond_num[2]}){op3}{correspond_num[3]}",
                                f"({correspond_num[0]}{op1}({correspond_num[1]}{op2}{correspond_num[2]})){op3}{correspond_num[3]}",
                                f"{correspond_num[0]}{op1}(({correspond_num[1]}{op2}{correspond_num[2]}){op3}{correspond_num[3]})",
                                f"{correspond_num[0]}{op1}({correspond_num[1]}{op2}({correspond_num[2]}{op3}{correspond_num[3]}))",
                                f"(({correspond_num[0]}{op1}{correspond_num[1]}){op2}({correspond_num[2]}{op3}{correspond_num[3]}))"
                            ]
                            for calculation_order in calculation_orders:
                                if verification(calculation_order):
                                    solutions.add(calculation_order)
    return solutions


import random

list_of_cards = list(card_number.keys()) * 4
random.shuffle(list_of_cards)
selected_cards = random.sample(list_of_cards, 4)
print(f"选中的牌：{selected_cards}")

solutions = operator_solutions(selected_cards)
if solutions:
    print("可能的情况：")
    for solution in solutions:
        print(solution)
else:
    print("无可能组合")