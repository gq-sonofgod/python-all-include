import os
 
class BatchRename():
    '''
    批量重命名文件夹中的图片文件
    '''
    def __init__(self):
        self.path = 'C:\\Users\\Administrator\\Desktop\\rename'  #表示需要命名处理的文件夹
 
    def rename(self):
        filelist = os.listdir(self.path)      #获取文件路径
        total_num = len(filelist)     #获取文件长度（个数）
        i = 1                     #表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'DLX_'+str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print ('将 %s 重命名为： %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('总共重命名 %d 个文件' % total_num)
 
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()