import csv
import datetime
import random

from constants import Category, Data

NUM_LINES = 10_000


class GenerateSampleData:
    def __init__(self, num_lines=NUM_LINES) -> None:
        self.num_lines = num_lines
        self.path = 'data/sample_data.csv'

    def generate_random_date(self, start_date, end_date):
        if start_date > end_date:
            raise Exception

        delta_days = (end_date - start_date).days
        random_date = start_date + datetime.timedelta(days=random.randrange(delta_days))
        return random_date.strftime(Data.DATE_FORMAT)

    def generate_random_category_id(self):
        category_ids = list(Category.CATEGORY_MAPPING.keys())
        return random.choice(category_ids)

    def generate_random_amount(self):
        random_amount = random.randrange(start=10_000, stop=1_000_000)
        return round(random_amount, -3)

    def generate_data_line(self):
        date = self.generate_random_date(
            start_date=datetime.date(2024, 10, 1), end_date=datetime.date(2024, 10, 31)
        )
        category_id = self.generate_random_category_id()
        amount = self.generate_random_amount()
        note = "test"
        return [date, category_id, amount, note]

    def generate_data(self):
        for _ in range(self.num_lines):
            yield self.generate_data_line()

    def generate_data_file(self):
        with open(self.path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)

            headers = Data.HEADERS
            writer.writerow(headers)
            for row in self.generate_data():
                writer.writerow(row)
