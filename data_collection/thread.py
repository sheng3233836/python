import os, threading


def append_to_csv(str_result):
    f = open("thread_test.txt", 'ab+')
    for i in range(100):
        f.write(str_result)
    f.write("\n")
    f.close()


def start_thread():
    thread_list = []
    for i in range(4):
        t = threading.Thread(target=append_to_csv, args=str(i))
        t.setDaemon(True)
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    # print(range(4))
    start_thread()
