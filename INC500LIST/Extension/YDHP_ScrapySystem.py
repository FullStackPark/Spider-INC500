import logging
import datetime


class ScrapySystem:
    @staticmethod
    def spider_work_finished(spider_name):
        logging.info(spider_name + "" + str(datetime.datetime.now()) + " Finished his work")

    @staticmethod
    def unit_test_finished():
        logging.info('[YDHP][Congratulation] All Unit Test Succeed ! + Module: `%s`')

    @staticmethod
    def test_failed(module_name):
        if type(module_name) is str:
            ScrapySystem.what_the_fxxk(module_name + " has some problems")
        else:
            ScrapySystem.what_the_fxxk("I can't understand the module name: `%s`" % str(module_name))

    @staticmethod
    def test_passed(module_name):
        if type(module_name) is str:
            logging.info("[YDHP][Congratulation] Unit Test Passed ! + Test: `%s`" % module_name)
        else:
            ScrapySystem.what_the_fxxk("I can't understand the Test name: `%s`" % str(module_name))

    @staticmethod
    def module_passed(module_name):
        if type(module_name) is str:
            logging.info('[YDHP][Congratulation] Unit Test Passed ! + Module: `%s`' % module_name)
        else:
            ScrapySystem.what_the_fxxk("I can't understand the Module name: `%s`" % str(module_name))

    @staticmethod
    def throw_exception(reason):
        if type(reason) is str:
            logging.error("[System Exception]:" + "For the reason that: `" + reason + "`")
            raise Exception("[System Exception]:" + "For the reason that: `" + reason + "`")
        else:
            logging.error("System Helper Exception: this is not a valid reason type")
            raise Exception("this is not a valid reason type")

    @staticmethod
    def what_the_fxxk(reason):
        ScrapySystem.throw_exception(reason)

