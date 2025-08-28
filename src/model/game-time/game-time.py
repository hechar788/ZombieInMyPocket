
class GameTime:
    """Keeps track of game time"""
    _AM = 'AM'
    _PM = 'PM'

    _START_TIME = 9
    _END_TIME = 12

    _INCREMENT = 1
    _TIME_DISPLAY_PREFIX = "The time is: "
    _TIME_DISPLAY_INFIX = ":00"


    def __init__(self):
        self._time: int = 9


    def __str__(self) -> str:
        """returns the current hour as a string"""
        return f"{self._TIME_DISPLAY_PREFIX}{self._time:02d}{self._TIME_DISPLAY_INFIX}{self._get_am_pm()}"


    def get_current_time_value(self) -> int:
        """returns the current hour as a number"""
        return self._time


    def increase_time(self) -> None:
        """Increases the time by one hour"""
        self._time += self._INCREMENT


    def is_time_valid(self) -> bool:
        """returns True if the current time is between 9 and 12"""
        return self._START_TIME < self._time < self._END_TIME


    def _get_am_pm(self):
        """returns the AM/PM time as a string"""
        if self._is_am():
            return self._AM
        else:
            return self._PM


    def _is_am(self):
        return self._time >= 12