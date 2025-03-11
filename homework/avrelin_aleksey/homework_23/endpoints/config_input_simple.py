class ConfQAPractice:
    id_submit = "id_text_string"
    id_text_result = "result-text"
    id_email = "id_email"
    id_password = "id_password"
    id_error_email = "error_1_id_email"
    id_error_password = "error_1_id_password"
    error_text_password = "Low password complexity"
    email_good = "aaalllweexx@ya.ru"
    email_bad = "sssssss22@222@sss.ru"
    email_error_text = "Enter a valid email address."
    good_password = "9p$7Px8esadaQHFJW1@#123"
    bad_password = "aaaaqqqq"
    input_data = "Aleksey"
    email_field = '(//li[@class="tab"]/a)[1]'
    password_field = '(//li[@class="tab"]/a)[2]'
    menu_inputs = "//ul[@class = 'sub-menu']/li[1]"
    menu_single_elements = "//li[@class='has-sub']/a"
    id_choose_language = "id_choose_language"
    select_choose_language = "//select[@id='id_choose_language']"
    id_submits = "id_text_string"
    xpath_submits = "//input[@id='submit-id-submit']"
    class_result_text = "result-text"
    menu_select = "//ul[@class = 'sub-menu']/li[4]"


class ConfigPracticeForm:
    FirstName = "Alex"
    LastName = "Mansem"
    UserEmail = "alex_mansem@ya.ru"
    mobile_number = "8911122233"
    month_name = "April"
    year = "2022"
    day = "15"
    subjects = "English"
    upload_file = "C:\\Users\\avrel\\Downloads\\2823965145.jpg"
    current_address = "Москва ул.Профсоюзная 80"
    gender = "Male"
    hobbies = "Sports"
    State = "Haryana"
    City = "Panipat"
    name_modal_header = "Thanks for submitting the form"

    xpath_radiobutton_male = (
        '(//div[@class="custom-control custom-radio custom-control-inline"]/label)[1]'
    )
    id_userEmail = "userEmail"
    id_firstName = "firstName"
    id_lastName = "lastName"
    id_mobile_number = "userNumber"
    id_calendar = "dateOfBirthInput"
    class_month = "react-datepicker__month-select"
    class_year = "react-datepicker__year-select"
    class_15_days = "react-datepicker__day--015"
    xpath_subjects = '//input[@id="subjectsInput"]'
    xpath_hobbies_sport = "//label[contains(text(), 'Sport')]"
    id_uploadPicture = "uploadPicture"
    id_current_address = "currentAddress"
    id_state = "state"
    id_state_haryana = "react-select-3-option-2"
    id_select_city = "city"
    id_city_panipat = "react-select-4-option-1"
    id_button_submit = "submit"
    id_modal_header = "example-modal-sizes-title-lg"


class PageElements:
    button_start = "//div[@id='start']/button"
    text_word = "//div/h4[text()='Hello World!']"
