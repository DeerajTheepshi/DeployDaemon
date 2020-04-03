import os
from dotenv import load_dotenv
from app.apache.apache import Apache

load_dotenv()


class php:
    httpd_path = ""

    def __init__(self, confName, port, serverName, serverAlias,
                 documentRoot, defaultConfFile):
        self.port = port
        self.confName = confName
        self.serverName = serverName
        self.serverAlias = serverAlias
        self.documentRoot = documentRoot
        self.httpd_path = os.getenv("HTTPD_PATH")

    def host(self):
        hostfile = Apache()
        hostfile.create_vhost(self.confName, self.port, self.serverName,
                              self.serverAlias, self.documentRoot)

    # change the default path using the template
    def changepath(self, documentRoot):
        temp = open("default_dir_template.txt", "r")
        change = temp.read().format(documentRoot=self.documentRoot)
        target = open(self.httpd_path + self.defaultConfFile, 'a')
        target.write(change)
        target.close()
        temp.close()

    def remove(self):
        rem = Apache()
        rem.delete_vhost(self.confName)
