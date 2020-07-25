class Constants:

    """
    Constant is class used to store all string literals
    """
    
    BILL = 'bill'
    BILL_PAY_LIMIT = 20000
    DEFAULT_EVENT_RULES = {
        'EventRuleA': 'Trigger a push notification on very first bill pay event for the user',
        'EventRuleB': 'Alert user if 5 or more bill pay events of total value >= 20000 happen within 5 minutes timewindow',
        'EventRuleC': 'Alert cube operator if bill paid, but did not give feedback within 15 minutes of the bill pay event'
    }
    ERROR = 'error'
    EXCEPTION_CODES = {
        'DEFAULT': [10000, 'There is some error in service, please try again'],
        'INVALID_REQUEST': [10001, 'Request data is invalid'],
        'DATABASE_READ_ERROR': [10002, 'An error occured while reading database'],
        'DATABASE_WRITE_ERROR': [10003, 'An error occured while writing in database'],
    }
    FEEDBACK = 'fdbk'
    FEEDBACK_TIME_LIMIT = 15
    MESSAGE = 'message'
    NOTIFY_TEXT_DICT = {
        'EventRuleA': 'NOTIFY:::This is very first bill pay event for the user.',
        'EventRuleB': 'ALERT-USER:::5 or more bill pay events of total value >= 20000 happened within 5 minutes timewindow.',
        'EventRuleC': 'ALERT-CUBE-OPERATOR:::Bill paid, but did not give feedback.'
    }
    NOUN = 'noun'
    PAY = 'pay'
    PROPERTIES = 'properties'
    POST = 'post'
    RESULT = 'result'
    RULE_NAME = 'rule_name'
    RULE_DESCRIPTION = 'rule_description'
    STATUS = 'status'
    TIMESTAMP = 'ts'
    USERID = 'userid'
    VALUE = 'value'
    VERB = 'verb'
