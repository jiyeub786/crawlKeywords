import crawler as cw
from module.logger import logger

def main():
    logger.info("----------main()----------")
    logger.info("start main()")
    cw.getResultKeywordFile()
    cw.getResultNewsFile()

    logger.info("end main()")


if __name__ == "__main__":
    main()



