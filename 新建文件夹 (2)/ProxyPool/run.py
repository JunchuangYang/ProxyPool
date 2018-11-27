from proxypool.scheduler import Scheduler
import sys
import io


# 改变标准输出的默认编码（这个比较重要一点，可以有效解决编码异常）
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()
