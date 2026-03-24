from webdriver_manager.core.driver import Driver
from webdriver_manager.core.logger import log
from webdriver_manager.core.os_manager import OSType, ChromeType


class EdgeChromiumDriver(Driver):

    def __init__(
            self,
            name,
            driver_version,
            url,
            latest_release_url,
            http_client,
            os_system_manager
    ):
        super(EdgeChromiumDriver, self).__init__(
            name,
            driver_version,
            url,
            latest_release_url,
            http_client,
            os_system_manager
        )

    def get_latest_release_version(self) -> str:
        """Get latest stable EdgeDriver version."""
        resp = self._http_client.get(url=self._latest_release_url)
        return resp.text.rstrip()

    def get_browser_type(self):
        return ChromeType.MSEDGE
