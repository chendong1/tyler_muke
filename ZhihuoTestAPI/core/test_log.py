import unittest
import config.conf_directory

if __name__ == '__main__':

    # 测试日志存放路径
    log_dir=config.conf_directory.log_dir

    #增加测试集
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestYzt))


    #写入测试日志
    with open(log_dir+'/Testlog.txt','a') as g:
        runner=unittest.TextTestRunner(stream=g,
                                       verbosity=2)
        runner.run(suite)
        g.close()