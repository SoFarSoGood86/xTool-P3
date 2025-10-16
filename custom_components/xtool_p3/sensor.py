from homeassistant.helpers.entity import Entity
class XTToolSensor(Entity):
    def __init__(self, name, coordinator):
        self._name = name
        self.coordinator = coordinator
    @property
    def name(self):
        return self._name
    @property
    def state(self):
        return self.coordinator.data.get('status')
