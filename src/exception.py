# # code from the video------
# import sys


# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     if exc_tb is None:
#         return str(error)

#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
#         file_name,exc_tb.tb_lineno,str(error)
#     )
#     return error_message
# class CustomException(Exception):
#     def __init__(self,error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)

#     def __str__(self):
#         return self.error_message

# chatgpt code
import sys
from types import TracebackType
from typing import Optional, Type


def error_message_detail(error: Exception, error_detail):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
