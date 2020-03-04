import os
import sys

import time
import threading

import crawler as cw
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.logger import logger
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
