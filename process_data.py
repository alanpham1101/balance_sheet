import csv
import datetime
import itertools
import operator
import pandas
import sys
import matplotlib.pyplot as plt

from constants import Category, Data, ProcessDataOption


class ReadDataFile:
    def __init__(self, data_path) -> None:
        self.data_path = data_path

    def refine_data(self, line):
        date = datetime.datetime.strptime(line['date'], Data.DATE_FORMAT).date()
        category_id = int(line['category_id'])
        category_name = Category.CATEGORY_MAPPING.get(category_id)
        amount = int(line['amount'])
        return [date, category_name, amount]

    def read_data_from_file(self):
        data = []
        with open(self.data_path, mode ='r') as csv_file:
            csv_file = csv.DictReader(csv_file)
            for line in csv_file:
                refined_data = self.refine_data(line)
                data.append(refined_data)

        self.data = data


class ProcessData(ReadDataFile):
    def process_data(self, option):
        try:
            option = int(option)
            if option == ProcessDataOption.NUMBER:
                self.process_data_with_number()
            elif option == ProcessDataOption.CHART:
                self.process_data_with_chart()
            else:
                raise Exception
        except Exception:
           sys.stdout.write("Invalid chosen option {option}".format(option=option))

    def process_data_with_number(self):
        sys.stdout.write("Process data with number\n======================\n")
        self.summarize_data_by_date()
        self.summarize_data_by_category()
        self.summarize_total()

    def process_data_with_chart(self):
        sys.stdout.write("Process data with chart\n=======================\n")
        df = pandas.DataFrame(
            sorted(self.data, key=operator.itemgetter(0)),
            columns = ['Date', 'Category', 'Amount']
        )

        # Group by 'Date' and sum the 'Amount' column
        df_date_grouped = df.groupby('Date')['Amount'].sum()

        # Group by 'Category' and sum the 'Amount' column
        df_category_grouped = df.groupby('Category')['Amount'].sum()

        # Create subplots: 1 row, 2 columns
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Plot for Date on the first subplot
        df_date_grouped.plot(kind='bar', ax=axes[0], color='blue')
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Total Amount')
        axes[0].set_title('Total Amount by Date')
        axes[0].tick_params(axis='x', rotation=45)

        for i, value in enumerate(df_date_grouped):
            axes[0].text(i, value + 20, "{value:,}".format(value=value), ha='center', fontsize=6)

        # Plot for Category on the second subplot
        df_category_grouped.plot(kind='bar', ax=axes[1], color='orange')
        axes[1].set_xlabel('Category')
        axes[1].set_ylabel('Total Amount')
        axes[1].set_title('Total Amount by Category')
        axes[1].tick_params(axis='x', rotation=0)

        for i, value in enumerate(df_category_grouped):
            axes[1].text(i, value + 10, "{value:,}".format(value=value), ha='center', fontsize=6)

        plt.tight_layout()
        plt.show()

    def summarize_data_by_date(self):
        grouped_data = ""
        date_ig, amount_ig = operator.itemgetter(0), operator.itemgetter(2)
        for date, group_data in itertools.groupby(sorted(self.data, key=date_ig), key=date_ig):
            total_amount = sum(map(amount_ig, group_data))
            grouped_data += "{date}: {total_amount:,}\n".format(
                date=date,
                total_amount=total_amount
            )

        sys.stdout.write("Summarize by date\n======================\n")
        sys.stdout.write(grouped_data + "\n")

    def summarize_data_by_category(self):
        grouped_data = ""
        category_ig, amount_ig = operator.itemgetter(1), operator.itemgetter(2)
        for category_name, group_data in itertools.groupby(sorted(self.data, key=category_ig), key=category_ig):
            total_amount = sum(map(amount_ig, group_data))
            grouped_data += Data.DATA_BY_CATEGORY.format(
                category_name=category_name,
                total_amount=total_amount
            )

        sys.stdout.write("Summarize by category\n======================\n")
        sys.stdout.write(grouped_data + "\n")

    def summarize_total(self):
        amount_ig = operator.itemgetter(2)
        total_amount = sum(map(amount_ig, self.data))
        total = "Total: {total_amount:,}\n".format(total_amount=total_amount)
        sys.stdout.write(total)
