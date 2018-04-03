#!/usr/bin/env python3
# coding=utf-8

import json

max_size = 0
db_name_set = set()
new_table_json_list = []
true_table_list = []
order_field_list = ["update_time", "dt_update", "dt_modify", "modify_time", "create_time", "createtime", "insert_time",
                    "dt_create", "dt_created", "day", "createTime", "oper_time", "insert_date", "create_date",
                    "created_time"]
with open("part2.json", "r") as file:
    table_json_list = json.load(file)
    for table in table_json_list:
        col = table["col"]
        col_list = col.split(",")
        for order in order_field_list:
            if order in col_list:
                table["totalData"] = "False"
                table["order"] = order
                break
            if order.upper() in col_list:
                table["totalData"] = "False"
                table["order"] = order
                break
        if table["totalData"] == "":
            table["totalData"] = "True"
            true_table_list.append(table)
        new_table = table.copy()
        db_name_set.add(table["dbName"])
        new_table.pop("size")
        new_table_json_list.append(new_table)

for db_name in db_name_set:
    single_table_json_list = []
    [single_table_json_list.append(table) for table in new_table_json_list if table['dbName'] == db_name]
    print(db_name + ":" + str(single_table_json_list.__len__()))
    with open(db_name + ".json", "w") as new_file:
        json.dump(single_table_json_list, new_file, indent=2)

# for table in true_table_list:
#     if max_size < float(table["size"]):
#         max_size = float(table["size"])
# print(max_size)
# print(new_table_json_list.__len__())
# print(true_table_list.__len__())

# true_table_list.sort(key=lambda d: float(d["size"]))
# true_table_list.reverse()
#
# [print(table) for table in true_table_list]

# with open("part2_new.json", "w") as new_file:
#     json.dump(new_table_json_list, new_file)
