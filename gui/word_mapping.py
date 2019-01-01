import json
import jieba
import xlwt
import time
import logging.config
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

jieba.set_dictionary("./dict.txt")
jieba.initialize()

aim_file_name = ""


def open_file():
    global aim_file_name
    aim_file_name = filedialog.askopenfilename(title='打开txt文件', filetypes=[('txtout', '*.txt')])
    logger.info(aim_file_name)
    Label(root, text=aim_file_name, font='Helvetica -12 bold').place(x=120, y=40)  # 创建标签


def mapping():
    try:
        detail_result_dict = {}
        result_dict = {}
        split_line_list = []
        if aim_file_name == "":
            messagebox.askokcancel('请先选择文件', '请先选择文件！请先选择文件！请先选择文件！')
        else:
            with open(aim_file_name, 'r', encoding='gbk') as file:
                logger.info(file.name + " 开始" + "自动分词" if var.get() == 1 else "手动分词")
                for line in file.readlines():
                    if var.get() == 1:
                        split_line_list.append("/".join(jieba.cut(line)))
                        line = " ".join(jieba.cut(line))
                    line = format_line(line)
                    for word in line:
                        if word != " ":
                            mapping_str(word, result_dict, detail_result_dict, '单字')
                    for phrase in re.split(r" +", line):
                        if phrase != "":
                            mapping_str(phrase, result_dict, detail_result_dict, '词语')
                logger.info(result_dict)
                Label(root, text="单字匹配结果:" + str(result_dict['单字']), font='Helvetica -12 bold').place(y=185)  # 创建标签
                Label(root, text="词语匹配结果:" + str(result_dict['词语']), font='Helvetica -12 bold').place(y=225)  # 创建标签
                output_excel(result_dict, detail_result_dict, split_line_list)
    except Exception:
        logger.error("报错啦！报错啦！", exc_info=1)


# 匹配字符
def mapping_str(word, result_dict, detail_result_dict, mapping_type='单字'):
    lib_list = mapping_type  # 单字 词语
    if lib_list not in result_dict:
        result_dict[lib_list] = {}
    if lib_list not in detail_result_dict:
        detail_result_dict[lib_list] = {}

    for lib_str in word_json[lib_list]:  # 级别
        if lib_str not in result_dict[lib_list]:
            result_dict[lib_list][lib_str] = 0
        if lib_str not in detail_result_dict[lib_list]:
            detail_result_dict[lib_list][lib_str] = {}

        if word in word_json[lib_list][lib_str]:
            result_dict[lib_list][lib_str] = result_dict[lib_list][lib_str] + 1

            if word in detail_result_dict[lib_list][lib_str].keys():
                detail_result_dict[lib_list][lib_str][word] = detail_result_dict[lib_list][lib_str][word] + 1
            else:
                detail_result_dict[lib_list][lib_str][word] = 1
            break
    else:
        if "超纲" in result_dict[lib_list]:
            result_dict[lib_list]["超纲"] = result_dict[lib_list]["超纲"] + 1
        else:
            result_dict[lib_list]["超纲"] = 1

        if "超纲" not in detail_result_dict[lib_list]:
            detail_result_dict[lib_list]["超纲"] = {}

        if word in detail_result_dict[lib_list]["超纲"]:
            detail_result_dict[lib_list]["超纲"][word] = detail_result_dict[lib_list]["超纲"][word] + 1
        else:
            detail_result_dict[lib_list]["超纲"][word] = 1


def format_line(line):
    return re.sub('[^\u4e00-\u9fff| *]', '', line)


def output_excel(result_dict, detail_result_dict, split_line_list):
    file_name = aim_file_name.split("/")[-1].split(".")[0]
    wb = xlwt.Workbook(encoding='gbk')
    for lib_str in ['单字', '词语']:
        sheet = wb.add_sheet(lib_str + '匹配结果', cell_overwrite_ok=True)
        sheet.write(0, 0, str(result_dict[lib_str]))
        i = 1
        for lib in detail_result_dict[lib_str]:
            for word in detail_result_dict[lib_str][lib]:
                sheet.write(i, 0, lib)
                sheet.write(i, 1, word)
                sheet.write(i, 2, detail_result_dict[lib_str][lib][word])
                i += 1
        if split_line_list != [] and lib_str == '词语':
            sheet.write(0, 5, "分词结果如下('/'为分词符)：")
            a = 1
            for split_line in split_line_list:
                sheet.write(a, 5, split_line)
                a += 1
    wb.save(file_name + '_详情结果_' + time.strftime("%Y%m%d%H%M%S") + '.xls')


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

    var = IntVar()
    Checkbutton(root, text="开启自动分词", font=("宋体", 13), variable=var, onvalue=1, offvalue=0).place(x=140, y=102)

    Label(root, text="——————————————————————————————————————————————————", font='Helvetica -12 bold').place(y=140)
    Label(root, text="结果展示", font='Helvetica -12 bold').place(x=200, y=155)

    root.mainloop()
