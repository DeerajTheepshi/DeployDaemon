import os

from app.apache.apache import Apache
from app.apache.proxyPass import ProxyPass


class Composer:

    def setup(self):
        os.system('composer install')
        os.system('php artisan key:generate')
        os.system('php artisan migrate')

    def seed(self):
        os.system('php artisan db:seed')

    def start(self, serverName=None, port=None):
        runServer = 'php artisan serve' \
            + (' --host=' + serverName if serverName else '') \
            + (' --port=' + port if port else '')
        os.system(runServer)
    
    def restart(self, serverName+None, port=None):
        stopServer = 'sudo kill $(sudo lsof -t' \
            + (' -i:' + port if port else '8000') \
            + ')'
        os.system(stopServer)
        self.start(serverName, port)

    def host(self, confName, port, serverName, serverAlias,
             documentRoot, route, urlToMap, priority):
        server = Apache()
        server.create_vhost(confName, port, serverName,
                            serverAlias, documentRoot)
        proxy = ProxyPass()
        proxy.addProxyPass(confName, route, urlToMap, priority)
