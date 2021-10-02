import unittest
from hideme.proxy_collector import ProxiesList

class HideMeTest(unittest.TestCase):

    def test_count_param_with_two(self):
        proxies = len(ProxiesList().get(count=2))
        self.assertGreaterEqual(proxies,2,"Count filter for 2 proxies failed.")

    def test_count_param_with_twenty(self):
        proxies = len(ProxiesList().get(count=20))
        self.assertGreaterEqual(proxies,20,"Count filter for 20 proxies failed.")

    def test_country_filter(self):
        proxy = ProxiesList(country='United States').get()
        self.assertEqual(proxy[0]['country'],'United States',"Country filter failed")

    def test_country_and_https_filter(self):
        proxy = ProxiesList(country='United States',https=False).get()
        self.assertEqual(proxy[0]['country'], 'United States', "Country and https filter failed")
        self.assertEqual(proxy[0]['https'], False, "Country and https filter failed")

    def test_multiple_filter(self):
        proxies_list = ProxiesList(country='United States', https=True, port='80', google_support=False)
        proxies = proxies_list.get()
        self.assertGreaterEqual(len(proxies),1,"Multiple Filters did not work")

    def test_no_count_value_passed(self):
        proxies_list = ProxiesList()
        proxies = proxies_list.get()
        self.assertGreaterEqual(len(proxies),295,"Greater than proxies were not returned")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(HideMeTest('test_count_param_with_two'))
    suite.addTest(HideMeTest('test_count_param_with_twenty'))
    suite.addTest(HideMeTest('test_country_filter'))
    suite.addTest(HideMeTest('test_country_and_https_filter'))
    suite.addTest(HideMeTest('test_multiple_filter'))
    suite.addTest(HideMeTest('test_no_count_value_passed'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())