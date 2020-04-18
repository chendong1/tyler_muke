import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import config.conf_directory
from core.test_getNewReport import get_NewReport
from core.test_mail import send_Mail

if __name__ == "__main__":

    # 测试用例路径
    test_dir = config.conf_directory.test_dir

    # 测试报告存放路径
    report_dir = config.conf_directory.report_dir

    #增加测试集
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    #当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #文件名称=目录+result+当前时间+后缀
    filename = report_dir + 'result-' + now + '.html'
    print (filename)
    #写入html测试报告
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='自动化测试报告', description='用例执行情况', verbosity=2)
        runner.run(discover)
        f.close()