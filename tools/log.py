import sys
import time


def write_log(log_content):
    path = sys.path[0] + '/log.txt'
    f = open(path, 'a+', encoding='utf8')
    log_content = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + __name__ + ' ==== ' + log_content + '\n'
    f.write(log_content)
    f.close()