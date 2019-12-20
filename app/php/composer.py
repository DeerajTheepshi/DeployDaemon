import os

from app.apache.apache import Apache
from app.apache.proxyPass import ProxyPass


class Composer:

    def run(self, serverName=None, port=None):
        os.system('composer install')
        os.system('php artisan key:generate')
        os.system('php artisan migrate')
        os.system('php artisan db:seed')
        runServer = 'php artisan serve' \
            + (' --host=' + serverName if serverName else '') \
            + (' --port=' + port if port else '')
        os.system(runServer)

    def host(self, confName, port, serverName, serverAlias,
             documentRoot, route, urlToMap, priority):
        server = Apache()
        server.create_vhost(confName, port, serverName,
                            serverAlias, documentRoot)
        proxy = ProxyPass()
        proxy.addProxyPass(confName, route, urlToMap, priority)
