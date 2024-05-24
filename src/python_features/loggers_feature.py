# Логгер настраивается 1 раз в 1 модуле. Все настройки наследуются от главного логгера,
# нужно только задать имя --> logger = getLogger(__name__)

from logging import getLogger, basicConfig, FileHandler, DEBUG, INFO, ERROR, StreamHandler

FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'

logger = getLogger()
file_handler = FileHandler("app.log", mode='w')
file_handler.setLevel(DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(ERROR)
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, stream_handler])


def calculate(expr):
    logger.debug('Get an expression - %s', expr)
    try:
        res = eval(expr)
        logger.debug('Calculating result - %s', res)
        return res
    except Exception as e:
        logger.error('Exception %s', e)


def start_app():
    while True:
        expression = input('Input expression for calculating: ')
        logger.debug('Expression is %s', expression)
        if not expression:
            logger.info('Expression is empty')
            break
        res = calculate(expression)
        if res is None:
            logger.info('Result is None')
            break
        print(f'Result is {res}')


if __name__ == '__main__':
    logger.info('service start working')
    start_app()
    logger.info('service end working')
