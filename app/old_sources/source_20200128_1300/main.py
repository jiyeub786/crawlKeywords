import crawler as cw
from module.logger import logger
import os

base_dir = os.path.dirname( os.path.abspath( __file__ ) ) +"\\files\\"

def main():
    logger.info("start crawler")
    crawl = [cw.setHeader(),cw.getNaver(),cw.getDaum(),cw.getYoutube()]
    for c in crawl:
        c
    logger.info("end crawler")




if __name__ == "__main__":
    main()