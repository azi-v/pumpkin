import threading

class MyThread(threading.Thread):
    def __init__(self, task, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.task = task
        super().__init__()

    def run(self) -> None:
        self.task(self.args, self.kwargs)

if __name__ == '__main__':
    ths = []
    for i in range(10):  # 批量任务例子
        task = lambda a,b: a+b # task 函数例子
        th = MyThread(task,i,i)
        th.start()
        ths.append(th)
    
    for t in ths:
        t.join()