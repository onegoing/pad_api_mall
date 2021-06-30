import datetime
import time
import unittest
from urllib.parse import quote
import requests
import my_variable


class TestApiMall(unittest.TestCase):

    base_url = "http://139.159.145.191:8302"

    def setUp(self):
        # 打印分割线
        print(">" * 35)
        # 输出测试开始时间
        self.start_time = datetime.datetime.now()
        print("测试开始时间：", self.start_time.strftime("%Y-%m-%d %H:%M:%S"))

    # 测试结束时间
    def tearDown(self):
        # 输出测试结束时间
        self.end_time = datetime.datetime.now()
        print("测试结束时间：", self.end_time.strftime("%Y-%m-%d %H:%M:%S"))
        spend_time = self.end_time - self.start_time
        spend_second = spend_time.total_seconds()
        print("测试用时：%.0f秒" % spend_second)

    # 登录接口
    def test_a_mall_login(self):
        """登录接口"""
        try:
            url_1 = "https://sitcmsapi.apfeg.com/Api/Login"

            # 登录账号信息
            data_1 = {
                        "userName": "HNXX0S202002003",
                        "password": "abc12345~"
                    }

            reply_1 = requests.post(url=url_1, data=data_1)
            assert "登录成功" in reply_1.json()["message"]
        except:
            print("接口1：登录接口测试，失败")
            raise
        else:
            print("接口1：登录接口测试，成功")
            my_variable.accessToken = "Bearer " + reply_1.json()["accessToken"]
            my_variable.per_id = reply_1.json()["data"]["userId"]

    # 获取登录账号信息接口
    def test_b_mall_account_message(self):
        """获取登录账号信息接口"""
        try:
            url_2 = "https://sitcmsapi.apfeg.com/Api/Personnel/GetStudentInfo"

            header_2 = {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Authorization": my_variable.accessToken
                       }

            data_2 = {
                "perId": my_variable.per_id
            }

            reply_2 = requests.post(url=url_2, data=data_2, headers=header_2)
            assert "查询成功" in reply_2.json()["message"]
        except:
            print("接口2：登录账号信息接口测试，失败")
            raise
        else:
            print("接口2：登录账号信息接口测试，成功")

    # 检测更新接口
    def test_c_mall_update(self):
        """检测更新接口"""
        try:
            url_3 = self.base_url + "/api/App/RenewableApp/com.future_education.marketplace/24"

            header_3 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            reply_3 = requests.get(url=url_3, headers=header_3)
            assert 200 == reply_3.status_code
        except:
            print("接口3：检测更新接口测试，失败")
            raise
        else:
            print("接口3：检测更新接口测试，成功")

    # 专属推荐接口
    def test_d_mall_recommand(self):
        """专属推荐接口"""
        try:
            url_4a = self.base_url + "/api/AppRecommend/QueryRecommendAppPage/0/6"
            url_4b = self.base_url + "/api/AppRecommend/QueryRecommendAppPage/0/10"

            header_4 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            try:
                reply_4a = requests.get(url=url_4a, headers=header_4)
                assert "操作成功" in reply_4a.json()["msg"]
            except:
                print("接口4：推荐页列表数据接口测试，失败")
                raise
            else:
                print("接口4：推荐页列表数据接口测试，成功")

            try:
                reply_4b = requests.get(url=url_4b, headers=header_4)
                assert "操作成功" in reply_4b.json()["msg"]
            except:
                print("接口5：推荐页更多列表数据接口测试，失败")
                raise
            else:
                print("接口5：推荐页更多列表数据接口测试，成功")
        except:
            raise

    # 新上架应用接口
    def test_e_mall_putaway(self):
        """新上架应用接口"""
        try:
            url_5a = self.base_url + "/api/AppRecommend/QueryLatestAppPage/0/6"
            url_5b = self.base_url + "/api/AppRecommend/QueryLatestAppPage/0/10"

            header_5 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            try:
                reply_5a = requests.get(url=url_5a, headers=header_5)
                assert "操作成功" in reply_5a.json()["msg"]
            except:
                print("接口6：新上架应用列表数据接口测试，失败")
                raise
            else:
                print("接口6：新上架应用列表数据接口测试，成功")

            try:
                reply_5b = requests.get(url=url_5b, headers=header_5)
                assert "操作成功" in reply_5b.json()["msg"]
            except:
                print("接口7：新上架应用更多列表数据接口测试，失败")
                raise
            else:
                print("接口7：新上架应用更多列表数据接口测试，成功")
        except:
            raise

    # 发现新事物接口
    def test_f_mall_new_thing(self):
        """发现新事物接口"""
        try:
            url_6a = self.base_url + "/api/AppRecommend/QueryFindNewAppPage/0/6"
            url_6b = self.base_url + "/api/AppRecommend/QueryFindNewAppPage/0/10"

            header_6 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            try:
                reply_6a = requests.get(url=url_6a, headers=header_6)
                assert "操作成功" in reply_6a.json()["msg"]
            except:
                print("接口8：发现新事物列表数据接口测试，失败")
                raise
            else:
                print("接口8：发现新事物列表数据接口测试，成功")

            try:
                reply_6b = requests.get(url=url_6b, headers=header_6)
                assert "操作成功" in reply_6b.json()["msg"]
            except:
                print("接口9：发现新事物更多列表数据接口测试，失败")
                raise
            else:
                print("接口9：发现新事物更多列表数据接口测试，成功")
                for each_name in reply_6b.json()["data"]["rows"]:
                    if "洋葱" in each_name["name"]:
                        my_variable.onion_id = each_name["id"]
        except:
            raise

    # 中小学商城-科目列表接口
    def test_g_mall_subjects(self):
        """中小学商城-科目列表接口"""
        try:
            url_7a = self.base_url + "/api/Subject/SubjectListPage"
            url_7b = self.base_url + "/api/Subject/AppSubjectPage/0/10/1"
            url_7c = self.base_url + "/api/Subject/AppSubjectPage/0/10/2"
            url_7d = self.base_url + "/api/Subject/AppSubjectPage/0/10/3"
            url_7e = self.base_url + "/api/Subject/AppSubjectPage/0/10/4"
            url_7f = self.base_url + "/api/Subject/AppSubjectPage/0/10/5"
            url_7g = self.base_url + "/api/Subject/AppSubjectPage/0/10/6"
            url_7h = self.base_url + "/api/Subject/AppSubjectPage/0/10/7"
            url_7i = self.base_url + "/api/Subject/AppSubjectPage/0/10/8"
            url_7j = self.base_url + "/api/Subject/AppSubjectPage/0/10/9"
            url_7k = self.base_url + "/api/Subject/AppSubjectPage/0/10/10"

            header_7 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            try:
                reply_7a = requests.get(url=url_7a, headers=header_7)
                first_sub = reply_7a.json()["data"][0]
                assert "语文" in first_sub.values()
            except:
                print("接口10：所有科目列表数据接口测试，失败")
                raise
            else:
                print("接口10：所有科目列表数据接口测试，成功")

            try:
                reply_7b = requests.get(url=url_7b, headers=header_7)
                assert 200 == reply_7b.status_code
            except:
                print("接口11：语文列表数据接口测试，失败")
                raise
            else:
                print("接口11：语文列表数据接口测试，成功")

            try:
                reply_7c = requests.get(url=url_7c, headers=header_7)
                assert 200 == reply_7c.status_code
            except:
                print("接口12：数学列表数据接口测试，失败")
                raise
            else:
                print("接口12：数学列表数据接口测试，成功")

            try:
                reply_7d = requests.get(url=url_7d, headers=header_7)
                assert 200 == reply_7d.status_code
            except:
                print("接口13：英语列表数据接口测试，失败")
                raise
            else:
                print("接口13：英语列表数据接口测试，成功")

            try:
                reply_7e = requests.get(url=url_7e, headers=header_7)
                assert 200 == reply_7e.status_code
            except:
                print("接口14：物理列表数据接口测试，失败")
                raise
            else:
                print("接口14：物理列表数据接口测试，成功")

            try:
                reply_7f = requests.get(url=url_7f, headers=header_7)
                assert 200 == reply_7f.status_code
            except:
                print("接口15：化学列表数据接口测试，失败")
                raise
            else:
                print("接口15：化学列表数据接口测试，成功")

            try:
                reply_7g = requests.get(url=url_7g, headers=header_7)
                assert 200 == reply_7g.status_code
            except:
                print("接口16：生物列表数据接口测试，失败")
                raise
            else:
                print("接口16：生物列表数据接口测试，成功")

            try:
                reply_7h = requests.get(url=url_7h, headers=header_7)
                assert 200 == reply_7h.status_code
            except:
                print("接口17：政治列表数据接口测试，失败")
                raise
            else:
                print("接口17：政治列表数据接口测试，成功")

            try:
                reply_7i = requests.get(url=url_7i, headers=header_7)
                assert 200 == reply_7i.status_code
            except:
                print("接口18：历史列表数据接口测试，失败")
                raise
            else:
                print("接口18：历史列表数据接口测试，成功")

            try:
                reply_7j = requests.get(url=url_7j, headers=header_7)
                assert 200 == reply_7j.status_code
            except:
                print("接口19：地理列表数据接口测试，失败")
                raise
            else:
                print("接口19：地理列表数据接口测试，成功")

            try:
                reply_7k = requests.get(url=url_7k, headers=header_7)
                assert 200 == reply_7k.status_code
            except:
                print("接口20：综合列表数据接口测试，失败")
                raise
            else:
                print("接口20：综合列表数据接口测试，成功")
        except:
            raise

    # 校园商城接口
    def test_h_mall_school(self):
        """校园商城接口"""
        try:
            url_8 = self.base_url + "/api/App/RenewableApp/com.future_education.marketplace/24"

            header_8 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            reply_8 = requests.get(url=url_8, headers=header_8)
            assert 200 == reply_8.status_code
        except:
            print("接口21：校园商城列表数据接口测试，失败")
            raise
        else:
            print("接口21：校园商城列表数据接口测试，成功")

    # 关键字搜索接口
    def test_i_mall_search(self):
        """关键字搜索接口"""
        try:
            key_search = quote("洋葱")
            url_9 = self.base_url + "/api/App/ApplicationSearchPage/0/50/" + key_search + "/0"

            header_9 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

            reply_9 = requests.get(url=url_9, headers=header_9)
            s_app = reply_9.json()["data"]["rows"][0]
            assert "洋葱" in s_app["name"]
        except:
            print("接口22：搜索app接口测试，失败")
            raise
        else:
            print("接口22：搜索app接口测试，成功")

    # 应用详情接口
    def test_j_mall_detail(self):
        """应用详情接口"""

        url_10a = self.base_url + "/api/App/FindDetails/" + str(my_variable.onion_id)
        url_10b = self.base_url + "/api/App/FindDetailCommentPage/" + str(my_variable.onion_id) + "/0/10"
        url_10d = self.base_url + "/api/AppComment/AddAppComment"

        header_10 = {
                        "Content-Type": "application/json;charset=utf-8",
                        "Authorization": my_variable.accessToken
                       }

        try:
            try:
                reply_10a = requests.get(url=url_10a, headers=header_10)
                assert "操作成功" in reply_10a.json()["msg"]
            except:
                print("接口23：查看应用详情接口测试，失败")

            else:
                print("接口23：查看应用详情接口测试，成功")

            try:
                reply_10b = requests.get(url=url_10b, headers=header_10)
                assert "操作成功" in reply_10b.json()["msg"]
            except:
                print("接口24：查看应用评价接口测试，失败")
                raise
            else:
                print("接口24：查看应用评价接口测试，成功")
                my_variable.comment_id = reply_10b.json()["data"]["rows"][0]["commentId"]

            try:
                url_10c = self.base_url + "/api/AppComment/AddUpdateAppCommentPraise" + str(my_variable.comment_id)
                reply_10c = requests.post(url=url_10c, headers=header_10)
                assert 200 == reply_10c.status_code
            except:
                print("接口25：点赞评论接口测试，失败")
                raise
            else:
                print("接口25：点赞评论接口测试，成功")

            try:
                # 新增评论时需要的参数
                # com_content = "新增评论{}".format(time.strftime("%Y-%m-%d %H:%M:%S"))
                json10d = {
                    "appId": my_variable.onion_id,
                    "commentId": my_variable.comment_id,
                    "content": "新增评论{}".format(time.strftime("%Y-%m-%d %H:%M:%S")),
                    "give": 0,
                    "isGive": False,
                    "level": 5
                        }
                reply_10d = requests.post(url=url_10d, headers=header_10, json=json10d)
                assert 200 == reply_10d.status_code
            except:
                print("接口26：新增评论接口测试，失败")
                raise
            else:
                print("接口26：新增评论接口测试，成功")
        except:
            raise





