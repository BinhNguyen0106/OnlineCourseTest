from page_locators.update_locator import UpdateLocator

class UpdatePage:
    def update_course(self, course_id, title, desc, price, cover):
        self.wait_for_element_visible(UpdateLocator.page_title, by="id")
        self.input(UpdateLocator.id_txt, course_id, by="id")
        self.input(UpdateLocator.title_txt, title, by="id")
        self.input(UpdateLocator.desc_txt, desc, by="id")
        self.input(UpdateLocator.price_txt, price, by="id")
        self.input(UpdateLocator.cover_txt, cover, by="id")
        self.click(UpdateLocator.update_btn, by="id")
