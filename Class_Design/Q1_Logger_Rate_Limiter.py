class Logger:
    def __init__(self):
        self.last_print_time = {}
        self.minimum_interval = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        is_message_previously_printed = message in self.last_print_time

        if not is_message_previously_printed:
            self.last_print_time[message] = timestamp
            return True
            
        last_timestamp_for_this_message = self.last_print_time[message]
        time_since_last_print = (timestamp - last_timestamp_for_this_message)

        if time_since_last_print < self.minimum_interval: return False
        self.last_print_time[message] = timestamp
        return True


if __name__ == '__main__':
    logger = Logger()
    print(logger.shouldPrintMessage(1, 'foo'))
    print(logger.shouldPrintMessage(2, 'bar'))
    print(logger.shouldPrintMessage(3, 'foo'))
    print(logger.shouldPrintMessage(8, 'bar'))
    print(logger.shouldPrintMessage(10, 'foo'))
    print(logger.shouldPrintMessage(11, 'foo'))



