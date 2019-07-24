import threading
import time

def run():

    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)   #设置守护线程，setDaemon()需要在start()之前
        t.start()

    for t in thread_list:
        t.join()    #确保主线程在全部子线程结束之后再退出

    print('主线程结束了！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)
