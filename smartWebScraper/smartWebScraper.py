import requests
from bs4 import BeautifulSoup
import csv
import re
from dateutil import parser


class SmartWebScraper:
    def __init__(self, url, filename="data.csv", empty_as_na=True):
        self.url = url
        self.filename = filename
        self.empty_as_na = empty_as_na

    def parse_html(self):
        # get response from the URL
        response = requests.get(self.url)
        response.raise_for_status()
        contents = response.text

        # put the content in our BeautifulSoup html parser
        soup = BeautifulSoup(contents, 'html.parser')
        return soup

    @staticmethod
    def extract_date(text):
        try:
            date = parser.parse(text, fuzzy=True)
            return date.date()
        except ValueError:
            return None

    @staticmethod
    def extract_price(text):
        pattern = r'(\d+(\.\d{2})?|\.\d{2})'  # Regular expression pattern to match the price format
        match = re.search(pattern, text)

        if match:
            price = match.group(0)
            return price
        else:
            return ''

    def export_to_csv(self, repeater_selector, fields):

        data_to_save = []
        soup = self.parse_html()
        elements = soup.select(selector=repeater_selector)
        if len(elements) < 0:
            return {
                "success": False,
                "message": "Your repeater selector does not have any elements"
            }

        for element in elements:
            curr_data = []
            for field in fields:
                curr_element = element.select(selector=field[1])

                if field[2] == "text":
                    try:
                        if len(field) > 3:
                            if field[3] == "price":
                                curr_data.append(self.extract_price(curr_element[0].text.strip()))
                            elif field[3] == "date":
                                curr_data.append(self.extract_date(curr_element[0].text.strip()))
                            else:
                                curr_data.append(curr_element[0].text.strip())
                        else:
                            curr_data.append(curr_element[0].text.strip())

                    except IndexError as err:
                        if self.empty_as_na:
                            curr_data.append('N/A')
                        else:
                            curr_data.append('')
                else:
                    try:
                        curr_data.append(curr_element[0].get(field[2]))
                    except IndexError as err:
                        if self.empty_as_na:
                            curr_data.append('N/A')
                        else:
                            curr_data.append('')

                data_to_save.append(curr_data)

        headers = [field[0] for field in fields]

        try:
            with open(self.filename, 'w', newline='') as file:
                # Create a CSV writer object
                writer = csv.writer(file)

                # Write the headers
                writer.writerow(headers)

                # Write the data rows
                writer.writerows(data_to_save)

            return {
                "success": True,
                "message": f"CSV file {self.filename} created successfully."
            }

        except PermissionError as err:
            return {
                "success": False,
                "message": f"The file {self.filename} you are trying to write is used by another program. "
                           f"Change the filename or close any program using this file"
            }
