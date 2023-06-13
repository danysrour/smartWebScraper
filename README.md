# Smart Web Scraper

This Python script allows you to smartly scrape data from a web page and export it to a CSV file. 

It utilizes the **requests, BeautifulSoup, re, and dateutil** libraries to retrieve and parse HTML content, extract specific fields, and handle dates and prices. 

# Features

- Retrieves HTML content from a specified URL using the requests library.
- Parses the HTML content using BeautifulSoup to extract desired information.
- Extracts dates from text using the extract_date method, leveraging the dateutil library.
- Extracts prices from text using the extract_price method, using regular expressions.
- Exports the extracted data to a CSV file, allowing customization of repeater selector and fields.
- Handles cases where the repeater selector does not have any elements or the output file is being used by another program.

# Usage

```python
from smartWebScraper import SmartWebScraper

scraper = SmartWebScraper(
    # change the URL_TO_SCRAPE with your url
    url="URL_TO_SCRAPE",
    # optional, default to True, mark as False if you want empty field to be empty instead of N/A
    empty_as_na=False,
    # optional, default to data.csv
    filename='test.csv'
)

# the below is an example of fields to be passed
# use your own
# list of tuples
# first element ex: Title is the header column name in the csv file
# second element ex: h3.bc-heading is the field selector use any selector you want you can use tags, classes or ids etc...
# third element ex: text is telling the program what to extract use text to extract text or use attribute name ex: href
# fourth element is optional. Add if you want to tell the program to treat this field as price or datetime (will extract the price or datetime automatically)
fields = [
            ('Title', 'h3.bc-heading', 'text'),
            ('Sub Title', 'li.bc-list-item.subtitle span', 'text'),
            ('Author', 'span.bc-text.bc-size-small.bc-color-secondary a', 'text'),
            ('Author Link', 'span.bc-text.bc-size-small.bc-color-secondary a', 'href'),
            ('Link', 'h3.bc-heading a.bc-link', 'href'),
            ('Image', '.bc-image-inset-border', 'src'),
            ('Length', 'li.bc-list-item.runtimeLabel', 'text'),
            ('Date', 'li.bc-list-item.releaseDateLabel span', 'text', 'date'),
            ('Language', 'li.bc-list-item.languageLabel', 'text'),
            ('Price', '.buybox-regular-price', 'text', 'price'),
         ]
# scraper.export_to_csv method take the repeater_selector (the selector of the repeated elements and the fields you created above)
result = scraper.export_to_csv(repeater_selector='li.bc-list-item.productListItem', fields=fields)
print(result)

```

## output

```text
{'success': True, 'message': 'CSV file test.csv created successfully.'}
```

# Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on [GitHub](https://github.com/danysrour/smartWebScraper.git).

# License

This project is licensed under the MIT License

```text

You can now copy this code and use it as your README.md file.
```