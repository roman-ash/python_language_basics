import json
with open("text_7.txt", "r") as f:
    company_profit_dict = {}
    sum_profit = 0
    num_of_profit_comp = 0
    for line in f:
        line_list = line.split()
        profit = int(line_list[2]) - int(line_list[3])
        print(f"{line_list[0]} company profit: {profit}")
        company_profit_dict[line_list[0]] = profit
        if profit > 0:
            sum_profit += profit
            num_of_profit_comp += 1
    average_profit = round(sum_profit / num_of_profit_comp, 1)
    print(f"Average profit of profitable companies: {average_profit}")
    average_profit_dict = {"average_profit": average_profit}
    my_list = [company_profit_dict, average_profit_dict]
    print(my_list)
    with open("json_text_7.json", "w") as x:
        json_list = json.dump(my_list, x)
