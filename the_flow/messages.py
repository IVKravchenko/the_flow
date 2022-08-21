"""
This file contains list of ERROR and WARNING messages and solutions which are used during THE FLOW execution.
Type of messages:
    [INIT-*]   - initialization part of THE FLOW
    [PHYGEN-*] - phy_gen messages
"""
import common_func


class messages:

    @staticmethod
    def init_1(dir_name, var_name):
        """
        ERROR : Directory * in * doesn't exist.

        :param dir_name: Directory name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        common_func.tf_error('[INIT-1] Directory "' +
                             dir_name +
                             '" in ' +
                             var_name +
                             ' doesn\'t exist.')
        common_func.tf_exit_with_error()

    @staticmethod
    def init_2(dir_name, var_name):
        """
        WARNING : Directory * in * doesn't exist.

        :param dir_name: Directory name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        common_func.tf_warning('[INIT-2] Directory "' +
                               dir_name +
                               '" in ' +
                               var_name +
                               ' doesn\'t exist.')

    @staticmethod
    def init_3(var_name):
        """
        ERROR : * variable name is invalid. Please, use variable names from template file.

        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        common_func.tf_error('[INIT-3] ' +
                             var_name +
                             ' variable name is invalid. Please, use variable names from template file.')
        common_func.tf_exit_with_error()

    @staticmethod
    def init_4(var_name):
        """
        ERROR : * doesn't define.

        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        common_func.tf_error('[INIT-4] ' +
                             var_name +
                             ' doesn\'t define.')
        common_func.tf_exit_with_error()

    @staticmethod
    def phygen_1(file_name, var_name):
        """
        ERROR : File * from * doesn't exist.

        :param file_name: File name.
        :param var_name: Variable name.
        :return: Text message into terminal window.
        """

        common_func.tf_error('[PHYGEN-1] File ' +
                             file_name +
                             ' from ' +
                             var_name +
                             ' doesn\'t exist.')
        common_func.tf_exit_with_error()
