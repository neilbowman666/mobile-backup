import ftplib
import os


class Ftp:
    ftp = ftplib.FTP()

    def __init__(self, host, port=9000):
        self.ftp.connect(host, port)

    def login(self, user, passwd):
        self.ftp.login(user, passwd)
        print(self.ftp.welcome)

    def delete_file(self):
        ...

    def download_file(self, remote_file, local_file):
        """
        下载文件
        :param remote_file:
        :param local_file:
        :return:
        """
        file_handler = open(local_file, 'wb')
        print(file_handler)
        # self.ftp.retrbinary("RETR %s" % (RemoteFile), file_handler.write) # 接收服务器上文件并写入本地文件
        self.ftp.retrbinary('RETR ' + remote_file, file_handler.write)
        file_handler.close()
        return True

    def download_file_tree(self, remote_dir, local_dir):
        """
        下载整个目录文件
        :param remote_dir:
        :param local_dir:
        :return:
        """
        print("remoteDir:", remote_dir)
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        self.ftp.cwd(remote_dir)
        remote_names = self.ftp.nlst()
        print("remote_names", remote_names)
        for file in remote_names:
            local = os.path.join(local_dir, file)
            print(self.ftp.nlst(file))
            if file.find(".") == -1:
                if not os.path.exists(local):
                    os.makedirs(local)
                self.download_file_tree(file, local)
            else:
                self.download_file(file, local)
        self.ftp.cwd("..")
        return

    def close(self):
        self.ftp.quit()


if __name__ == "__main__":
    ftp = Ftp('777.777.777.777', 21)
    ftp.login('anonymous', 'sss')
    ftp.download_file_tree('D:/test', '/DCIM/Camera')  # 从目标目录下载到本地目录d盘
    ftp.close()
    print("ok!")
