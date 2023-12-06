class CourseLocator:
    add_course_btn = "addHome"
    update_item_btn = "//a[@href = '/{id}']/./following-sibling::button[@id = 'buttonUpdate']"
    delete_item_btn = "//a[@href = '/{id}']/./following-sibling::button[@id = 'buttonDelete']"
    deleted_title_lbl = "//h2[@id = 'courseTitle' and text() = '{title}']"
    deleted_desc_lbl = "//p[@id = 'courseDescription' and text() = '{desc}']"
    title_lbl = "//a[@href = '/{id}']/h2"
    desc_lbl = "//a[@href = '/{id}']/./following-sibling::p[@id = 'courseDescription']"
    page_name_lbl = "pageName"
