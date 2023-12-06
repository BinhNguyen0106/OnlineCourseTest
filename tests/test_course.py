
from seleniumbase import BaseCase
from page_objects.course_page import CoursePage
from page_objects.add_page import AddPage
from page_objects.update_page import UpdatePage
from utils.utils import Utils

class CourseTest(BaseCase):


    def setUp(self):
        super().setUp()
        # open course page
        print("Open browser")
        CoursePage.open_page(self)

    def test_crud_course(self):
        # click on add new course button
        course_id = Utils.random_number(self)
        title = "Chemistry"
        desc = "Chemistry grade 9 description"
        price = "64"
        cover = "investor.jpg"

        CoursePage.go_to_add_page(self)
        AddPage.add_course(self, course_id, title, desc, price, cover)
        actual_title = CoursePage.get_title_text(self, course_id)
        actual_desc = CoursePage.get_desc_text(self, course_id)
        CoursePage.verify_title_of_added_course(self, title, actual_title)
        CoursePage.verify_description_of_added_course(self, desc, actual_desc)

        #update
        title = "Updated " + title
        desc = "Updated " + desc
        CoursePage.go_to_update_course_page(self, course_id)
        UpdatePage.update_course(self, course_id, title, desc, price, cover)

        #delete
        CoursePage.delete_item(self, course_id)
        self.sleep(10)
        CoursePage.verify_title_of_deleted_item_not_exist(self, title)
        CoursePage.verify_desc_of_deleted_item_not_exist(self, desc)

    def test_expected_error_on_page_name(self):
        # assert title
        expected_page_name = "Baa Course"
        actual_page_name = CoursePage.get_page_name_text(self)
        self.sleep(5)
        CoursePage.verify_page_name(self, expected_page_name, actual_page_name)

