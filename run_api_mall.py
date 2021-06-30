import os
import time
import unittest
from BeautifulReport import BeautifulReport


# 用例所在的路径
case_path = os.path.dirname(os.path.abspath(__file__)) + "/scripts"

# 定义测试套件
suite = unittest.defaultTestLoader.discover(case_path)

# 报告存储路径
report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/平板应用中心接口自动化测试报告"

# 报告的名称
# report_name = "{}.html".format(time.strftime("%Y_%m%d_%H:%M:%S"))

BeautifulReport(suite).report(report_dir=report_path, description="平板应用中心接口自动化测试")

