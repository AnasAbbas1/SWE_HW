class APIsInputValidator:
    _NUMBERS_PARAM = 'numbers'

    def __init__(self, data, quantifier_name):
        self.__init_input_validator(data, quantifier_name)

    def has_error(self):
        return hasattr(self, '_error') and self._error is not None

    def __get_error(self):
        return self._error

    def __validate_parameter_existence(self, data, parameter):
        if parameter not in data:
            self._error = {'error': f'missing required parameter: {parameter}'}
        elif not data[parameter]:
            self._error = {'error': f'required parameter: {parameter} cannot be empty'}

    def __validate_parameter_type(self, data, parameter, expected_type):
        if not isinstance(data[parameter], expected_type):
            self._error = {'error': f'{parameter} parameter must be of type {expected_type}'}

    def __validate_integer_parameter_value(self, data, parameter, min_value, max_value):
        if data[parameter] < min_value or data[parameter] > max_value:
            self._error = {'error': f'{parameter} parameter must be in range {min_value} to {max_value}'}

    def __validate_numbers_list_input(self, data):
        self.__validate_parameter_existence(data, self._NUMBERS_PARAM)
        if not self.has_error():
            self.__validate_parameter_type(data, self._NUMBERS_PARAM, list)
        if not self.has_error():
            for number in data[self._NUMBERS_PARAM]:
                if not isinstance(number, int):
                    self._error = {'error': f'{self._NUMBERS_PARAM} list must contain integers only'}

    def __validate_quantifier_integer_input(self, data, quantifier_name, max_value):
        self.__validate_parameter_existence(data, quantifier_name)
        if not self.has_error():
            self.__validate_parameter_type(data, quantifier_name, int)
        if not self.has_error():
            self.__validate_integer_parameter_value(data, quantifier_name, 0, max_value)

    def __init_input_validator(self, data, quantifier_name):
        self.__validate_numbers_list_input(data)
        if quantifier_name and not self.has_error():
            max_value = len(data[self._NUMBERS_PARAM]) if quantifier_name == 'quantifier' else 100
            self.__validate_quantifier_integer_input(data, quantifier_name, max_value)

    @staticmethod
    def validate_input(data, quantifier_name):
        validator = APIsInputValidator(data, quantifier_name)
        if validator.has_error():
            raise Exception(validator.__get_error())