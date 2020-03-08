import logging.handlers
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))
from config import config

log_path = config.LOG_PATH
log_file = "systemlog.log"
# LogFileNm
LogFileNm = log_path + log_file

#log level DEBUG, INFO, WARNING, ERROR, CRITICAL
    # logger 인스턴스를 생성 및 로그 레벨 설정
logger = logging.getLogger("crumbs")

#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
    # formmater 생성
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    # fileHandler와 StreamHandler를 생성
fileHandler = logging.FileHandler(LogFileNm,encoding='utf-8')
streamHandler = logging.StreamHandler()

    # handler에 fommater 세팅
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

    # Handler를 logging에 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
