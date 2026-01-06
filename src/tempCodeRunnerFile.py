    try:
        a=1/0
    except Exception as e:
            logging.info("Divide by zero")
            raise custom_exception(e,sys)