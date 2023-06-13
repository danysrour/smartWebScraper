from smartWebScraper import SmartWebScraper

scraper = SmartWebScraper(
    url="https://www.audible.com/search?keywords=book&node=18573211011",
    empty_as_na=False,
    filename='test.csv'
)

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
result = scraper.export_to_csv(repeater_selector='li.bc-list-item.productListItem', fields=fields)
print(result)
