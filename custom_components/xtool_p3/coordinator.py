from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
class XTToolCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api):
        super().__init__(hass, _LOGGER, name="xTool P3", update_interval=10)
        self.api = api
    async def _async_update_data(self):
        return await self.api.get_status()
