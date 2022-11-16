#创建一个日志器
import logging

def test_log():
    logger=logging.getLogger()
    #设置日志级别
    logger.setLevel(logging.INFO)
    #日志输出到控制台,创建一个控制台
    sh = logging.StreamHandler()
    #把日志信息输出到控制台
    logger.addHandler(sh)
    #创格式器
    fomart1='%(asctime)s %(filename)s %(levelname)s %(module)s %(message)s'
    #创建一个格式器
    formator = logging.Formatter(fomart1)
    #给控制台设置格式
    sh.setFormatter(formator)


    #把日志信息存到文件中
    fh = logging.FileHandler('../logs/log.log', encoding='utf-8')
    logger.addHandler(fh)
    #给文件设置格式
    fh.setFormatter(formator)
    return logger
#logger.info('信息级别')