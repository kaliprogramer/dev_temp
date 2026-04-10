
from channels.generic.websocket import AsyncWebsocketConsumer
import json
class AdminNotificationConsumer(AsyncWebsocketConsumer):
  async def connect(self):
      await self.channel_layer.group_add(
          "admin_group",
          self.channel_name
      )
      await self.accept()
  async def disconnect(self, close_code):
      await self.channel_layer.group_discard(
          "admin_group",
          self.channel_name
      )
  async def notify(self, event):
      await self.send(text_data=json.dumps(event["data"]))