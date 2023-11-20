class Utils:
    def isacommand(text:str):
        if str(text).startswith("/"):
            return True
        else:
            return False
