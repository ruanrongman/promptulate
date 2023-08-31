from typing import Union
from time import sleep

from promptulate.tools import BaseTool


class SleepTool(BaseTool):
    name: str = "sleep"
    description: str = (
        "Make agent sleep for a specified number of seconds."
        "Input is a number. eg: Sleep for 5s and enter 5"
    )

    def _run(
        self,
        sleep_time: Union[int, float],
    ) -> str:
        """Use the Sleep tool."""
        sleep(int(sleep_time))
        return f"Agent slept for {sleep_time} seconds."