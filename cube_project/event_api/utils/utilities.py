class Utilities:

    @staticmethod
    def get_modified_date(date_string):
        """
            date_string - 2020-07-24 17:38:08.537
            return - 20200724 173808
        """
        return date_string.split('.')[0].replace('-', '').replace(':', '')