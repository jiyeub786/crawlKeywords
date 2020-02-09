import crawler as cw
from module.logger import logger
import time
import threading

schd = ['09:00', '18:00', '00:00']


def main():
    logger.info("----------main()----------")
    logger.debug("start main()")
    cw.getResultKeywordFile()
   # cw.getResultNewsFile()
    logger.debug("end main()")


def thread_run():
    now = time.strftime('%H:%M', time.localtime(time.time()))
    print('running....' + now)
    for i, v in enumerate(schd):
        if v == now:
            main()
    threading.Timer(60, thread_run).start()


if __name__ == "__main__":
    #thread_run()  # 스케줄
     main()   # 바로실행
