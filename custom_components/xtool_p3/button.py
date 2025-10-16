from homeassistant.helpers.entity import Entity
class XTToolButton(Entity):
    def __init__(self, name, api, command):
        self._name = name
        self.api = api
        self.command = command
    @property
    def name(self):
        return self._name
    async def async_press(self):
        await self.api.send_command(self.command)
