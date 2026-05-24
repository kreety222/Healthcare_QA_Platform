from playwright.sync_api import sync_playwright


BASE_URL = "https://the-internet.herokuapp.com/upload"


class TestMedicalUploadUI:

    def test_upload_wrong_file_type(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(BASE_URL)

            page.set_input_files(
                "#file-upload",
                "data/invalid_file.exe"
            )

            page.click("#file-submit")

            error_message = (
                "Invalid file type"
            )

            assert (
                error_message
                == "Invalid file type"
            )

            browser.close()

    def test_upload_large_pdf(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(BASE_URL)

            page.set_input_files(
                "#file-upload",
                "data/large_medical_chart.pdf"
            )

            page.click("#file-submit")

            validation_message = (
                "File exceeds size limit"
            )

            assert (
                validation_message
                == "File exceeds size limit"
            )

            browser.close()

    def test_empty_file_upload(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(BASE_URL)

            page.click("#file-submit")

            validation_message = (
                "Please upload a file"
            )

            assert (
                validation_message
                == "Please upload a file"
            )

            browser.close()