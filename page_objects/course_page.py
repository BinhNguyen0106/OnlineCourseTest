import logging

from utils.utils import Utils
from utils.constants import Constants
from page_locators.course_locator import CourseLocator

class CoursePage:
    def go_to_add_page(self):
        self.scroll_into_view(CourseLocator.add_course_btn, by="id")
        self.click(CourseLocator.add_course_btn, by="id")

    def open_page(self):
        self.open(Constants.URL)

    def go_to_update_course_page(self, course_id):
        self.scroll_into_view(CourseLocator.update_item_btn.format(id=course_id), by="xpath")
        self.click(CourseLocator.update_item_btn.format(id=course_id), by="xpath")

    def delete_item(self, course_id):
        self.scroll_into_view(CourseLocator.delete_item_btn.format(id=course_id), by="xpath")
        self.click(CourseLocator.delete_item_btn.format(id=course_id), by="xpath")

    def verify_title_of_deleted_item_not_exist(self, title):
        logging.info("CoursePage - verify_title_of_deleted_item_not_exist - title: ", title)
        self.assert_element_not_visible(CourseLocator.deleted_title_lbl.format(title=title), by="xpath")

    def verify_desc_of_deleted_item_not_exist(self, desc):
        self.assert_element_not_visible(CourseLocator.deleted_desc_lbl.format(desc=desc), by="xpath")

    def get_title_text(self, course_id):
        return self.get_text(CourseLocator.title_lbl.format(id=course_id), by="xpath")

    def get_desc_text(self, course_id):
        return self.get_text(CourseLocator.desc_lbl.format(id=course_id), by="xpath")

    def verify_title_of_added_course(self, expected_title, actual_title):
        return self.assert_equal(expected_title, actual_title)

    def verify_description_of_added_course(self,expected_desc, actual_desc):
        return self.assert_equal(expected_desc, actual_desc)

    def get_page_name_text(self):
        logging.info("CoursePage - get_page_name_text")
        return self.get_text(CourseLocator.page_name_lbl, by="id")

    def verify_page_name(self, expected_result, actual_result):
        logging.info("CoursePage - verify_page_name")
        return self.assert_equal(expected_result, actual_result)
