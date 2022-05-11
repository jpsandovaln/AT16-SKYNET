import abc


class ValidatorStrategy(abc.ABC):

    @NotNull
    String name;

    def validate(self):
        """Validate method should be implemented"""
