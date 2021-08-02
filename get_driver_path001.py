def get_browser(*browser_name):
    """
    获取浏览器路径
    :param browser_name: 浏览器名称
    :return:
    """
    import os
    import re
    path = []
    registry = r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters"

    def query_the_registration_form(registry_address=registry):
        """
        查询注册表
        :param registry_address: 注册表地址
        :return:
        """
        data = os.popen(
            rf"reg query {registry_address}")
        data = data.read()
        data_s = data.split()
        for i in data_s:
            if "HKEY_LOCAL_MACHINE" in i and i not in registry_address:
                # print(i)
                query_the_registration_form(i)
            else:
                regular_match_browser_address(i)

    def regular_match_browser_address(da):
        """
        正则匹配得到浏览器路径
        :param da: 地址信息
        :return:
        """
        nonlocal path
        for i in browser_name:
            if i in da:
                da = re.findall(r'App=([\w:\\]+)', da)
                path += da

    def get_browser_address():
        """
        得到浏览器路径
        :return:
        """
        query_the_registration_form()
        for i in path:
            if os.path.exists(i + ".exe"):
                return i + ".exe"

    return get_browser_address()

if __name__ == '__main__':
    print(get_browser("360极速浏览器","360安全浏览器"))
