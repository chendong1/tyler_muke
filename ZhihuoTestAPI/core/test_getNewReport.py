import os

def get_NewReport(testreport):
    #获取testreport 目录下的文件返回一个list
    dirs = os.listdir(testreport)
    #对文件list 进行排序 进行增序排列
    dirs.sort()
    #获取序列最后一个元素，即最大的一个元素。
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport,newreportname)
    print(file_new)
    return file_new