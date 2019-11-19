import apache

PROXY_RULE = 'ProxyPass "{route}" "{urlToMap}" \n'
REV_PROXY_RULE = 'ProxyPassReverse "{route}" "{urlToMap}" \n'


class ProxyPass(apache.Apache):

    def __init__(self):
        super().__init__()

    # Add Proxy pass based on priority.
    # 1:Add on Top, 0:Add on Bottom
    # ISSUE : Better Parsing ideas are welcome
    def addProxyPass(self, confName, route, urlToMap, priority):
        targetFile = open(self.httpd_path + confName, 'r+')
        lines = targetFile.readlines()
        for i, line in enumerate(lines):
            if "proxyPass_Flag" in line and priority:
                print("ji")
                lines.insert(
                    i +
                    1,
                    "\t" +
                    PROXY_RULE.format(
                        route=route,
                        urlToMap=urlToMap))
                lines.insert(
                    i +
                    2,
                    "\t" +
                    REV_PROXY_RULE.format(
                        route=route,
                        urlToMap=urlToMap))

            if "proxyPassEnd_Flag" in line and not priority:
                lines.insert(
                    i -
                    2,
                    "\t" +
                    PROXY_RULE.format(
                        route=route,
                        urlToMap=urlToMap))
                lines.insert(
                    i -
                    1,
                    "\t" +
                    REV_PROXY_RULE.format(
                        route=route,
                        urlToMap=urlToMap))

        targetFile.seek(0)
        targetFile.writelines(lines)
        targetFile.truncate()
        targetFile.close()

        return None
