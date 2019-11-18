import os
from proxyPass import ProxyPass
from dotenv import load_dotenv

load_dotenv()


class Apache_ssl:
    httpd_path = ""

    def __init__(self):
        self.httpd_path = os.getenv("HTTPD_PATH")

    # create a vhost file from the template
    def create_vhost(
            self,
            confName,
            port,
            serverName,
            serverAlias,
            documentRoot,
            certPath,
            certKeyPath):
        template = open("base_template_ssl.txt", 'r')
        required = template.read().format(
            port=port,
            serverName=serverName,
            serverAlias=serverAlias,
            documentRoot=documentRoot,
            certPath=certPath,
            certKeyPath=certKeyPath)
        targetFile = open(self.httpd_path + confName, 'w')
        targetFile.write(required)
        targetFile.close()
        template.close()

        return None

    # Edit a given vhost config file
    # If changing certs, both key and cert should be changed
    # ISSUE : Better Parsing ideas are welcome
    def edit_vhost(
            self,
            confName,
            port=None,
            serverName=None,
            serverAlias=None,
            documentRoot=None,
            certPath=None,
            certKeyPath=None):
        targetFile = open(self.httpd_path + confName, 'r+')
        lines = targetFile.readlines()
        for i, line in enumerate(lines):
            if "serverName_Flag" in line and serverName:
                line_array = lines[i + 1].split()
                line_array[1] = serverName + "\n"
                lines[i + 1] = "\t" + " ".join(line_array)

            if "serverAlias_Flag" in line and serverAlias:
                line_array = lines[i + 1].split()
                line_array[1] = serverAlias + "\n"
                lines[i + 1] = "\t" + " ".join(line_array)

            if "documentRoot_Flag" in line and documentRoot:
                line_array = lines[i + 1].split()
                line_array[1] = documentRoot + "\n"
                lines[i + 1] = "\t" + " ".join(line_array)

            if "ssl_Flag" in line and certPath and certKeyPath:
                line_array = lines[i + 1].split()
                line_array[1] = certPath + "\n"
                lines[i + 1] = "\t" + " ".join(line_array)

                line_array = lines[i + 2].split()
                line_array[1] = certKeyPath + "\n"
                lines[i + 1] = "\t" + " ".join(line_array)

        targetFile.seek(0)
        targetFile.writelines(lines)
        targetFile.truncate()
        targetFile.close()

        return None

    def delete_vhost(self, confName):
        os.remove(self.httpd_path + confName)

        return None


# To test current module
if __name__ == '__main__':
    apache_ssl = Apache_ssl()
    apache_ssl.create_vhost(
        "test.com.conf",
        "8080",
        "test.com.conf",
        "sensors",
        "/srv/http/",
        "xyz",
        "xyz")
    apache_ssl.edit_vhost("test.com.conf", serverName="test.in")
    proxy = ProxyPass()
    proxy.addProxyPass("test.com.conf", "/", "http://ss:8000", 1)
    # apache.delete_vhost("test.conf.com")
