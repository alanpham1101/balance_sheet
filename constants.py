class Category:
    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    DATING = 4
    TRANSPORT = 5
    SNACK = 6
    HANGOUT = 7
    BILL = 8
    WEDDING = 9
    STUFF = 10

    CATEGORY_MAPPING = {
        BREAKFAST: 'Breakfast',
        LUNCH: 'Lunch',
        DINNER: 'Dinner',
        DATING: 'Dating',
        TRANSPORT: 'Transport',
        SNACK: 'Snack',
        HANGOUT: 'Hangout',
        BILL: 'Bill',
        WEDDING: 'Wedding',
        STUFF: 'Stuff'
    }


class Data:
    HEADERS = ['date', 'category_id', 'amount', 'note']
    DATE_FORMAT = '%Y-%m-%d'
    DATA_BY_DATE_FORMAT = '{date}: {total_amount:,}\n'
    DATA_BY_CATEGORY = '{category_name}: {total_amount:,}\n'


class ProcessDataOption:
    NUMBER = 1
    CHART = 2
