import json
import xlwt
import time
import logging.config
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

aim_file_name = ""
lib_str_arr = ["一级", "二级", "三级", "四级"]


def open_file():
    global aim_file_name
    aim_file_name = filedialog.askopenfilename(title='打开txt文件', filetypes=[('txtout', '*.txt')])
    logger.info(aim_file_name)
    Label(root, text=aim_file_name, font='Helvetica -12 bold').place(x=120, y=40)  # 创建标签


def mapping():
    try:
        beyond_list = []
        detail_result_dict = {"一级": {}, "二级": {}, "三级": {}, "四级": {}, "超纲": {}}
        result_dict = {"一级": 0, "二级": 0, "三级": 0, "四级": 0, "超纲": 0}
        if aim_file_name == "":
            messagebox.askokcancel('请先选择文件', '请先选择文件！请先选择文件！请先选择文件！')
        else:
            with open(aim_file_name, 'r', encoding='gbk') as file:
                logger.info(file.name + " start mapping")
                for line in file.readlines():
                    line = format_line(line)
                    for word in line:
                        mapping_str(word, result_dict, beyond_list, detail_result_dict)
                logger.info(result_dict)
                output_excel(result_dict, beyond_list, detail_result_dict)
                Label(root, text=str(result_dict), font='Helvetica -12 bold').place(y=185)  # 创建标签
    except Exception:
        logger.error("报错啦！报错啦！", exc_info=1)


# 匹配字符
def mapping_str(word, result_dict, beyond_list, detail_result_dict):
    for lib_str in lib_str_arr:
        if word in word_list[lib_str]:
            result_dict[lib_str] = result_dict[lib_str] + 1
            if word in detail_result_dict[lib_str].keys():
                detail_result_dict[lib_str][word] = detail_result_dict[lib_str][word] + 1
            else:
                detail_result_dict[lib_str][word] = 1
            break
    else:
        result_dict["超纲"] = result_dict["超纲"] + 1
        beyond_list.append(word)


def format_line(line):
    return re.sub('[^\u4e00-\u9fff]', '', line)


def output_excel(result_dict, beyond_list, detail_result_dict):
    file_name = aim_file_name.split("/")[-1].split(".")[0]
    wb = xlwt.Workbook(encoding='gbk')
    sheet = wb.add_sheet('汉字匹配结果', cell_overwrite_ok=True)
    sheet.write(0, 0, str(result_dict))
    i = 1
    for lib in detail_result_dict.keys():
        for word in detail_result_dict[lib].keys():
            sheet.write(i, 0, lib)
            sheet.write(i, 1, word)
            sheet.write(i, 2, detail_result_dict[lib][word])
            i += 1
    sheet.write(i, 0, "超纲")
    sheet.write(i, 1, beyond_list)
    wb.save(r'../' + file_name + '_详情结果_' + time.strftime("%Y%m%d%H%M%S") + '.xls')


if __name__ == "__main__":
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger()

    word_json = json.load(open("word.json", 'r', encoding='utf-8'))
    word_list = word_json['单字']

    root = Tk()
    root.title('文字匹配小工具')
    root.geometry('450x350')
    root.resizable(0, 0)

    Button(root, text='选择书籍', font=("宋体", 13), command=open_file).place(x=10, y=35)
    Button(root, text='开始匹配', font=("宋体", 13), command=mapping).place(x=350, y=100)

    Label(root, text="——————————————————————————————————————————————————", font='Helvetica -12 bold').place(y=140)
    Label(root, text="结果展示", font='Helvetica -12 bold').place(x=200, y=155)

    root.mainloop()
