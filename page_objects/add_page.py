from page_locators.add_locator import AddLocator

class AddPage:
    def add_course(self, course_id, title, desc, price, cover):
        self.wait_for_element_visible(AddLocator.page_title, by="id")
        self.input(AddLocator.id_txt, course_id, by="id")
        self.input(AddLocator.title_txt, title, by="id")
        self.input(AddLocator.desc_txt, desc, by="id")
        self.input(AddLocator.price_txt, price, by="id")
        self.input(AddLocator.cover_txt, cover, by="id")
        self.click(AddLocator.add_btn, by="id")
