import asyncio
from asyncua import Client, ua

class SubHandler(object):
    """
    Subscription Handler class to handle the incoming events asynchronously.
    """
    def event_notification(self, event):
        print("New event received:")
        print("Event Type:", event.EventType)
        print("Severity:", event.Severity)
        print("Message:", event.Message)
        if hasattr(event, 'LocaleIds'):
            print("Locale:", event.LocaleIds)
        print("-" * 20)

async def main():
    url = "opc.tcp://localhost:4840"  # Replace with your server address
    client = Client(url)
    try:
        await client.connect()
        print("Client Connected")

        # Create a subscription 
        subscription = await client.create_subscription(500, SubHandler())
        
        # Subscribe to Alarm & Condition events
        handle = await subscription.subscribe_events()

        # Ideally, Locale settings should be managed at session or server level,
        # but here's how we theoretically could attempt setting the locale_ids.
        # This may not be directly supported and might need a different approach based on server specifics:
        session = client.uaclient._uasocket
        session.default_request_params.locale_ids = ["mul"]

        print("Subscription created, listening for events...")
        await asyncio.Future()  # Run forever

    finally:
        await client.disconnect()
        print("Client disconnected")

if __name__ == "__main__":
    asyncio.run(main())