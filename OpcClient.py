import sys
from opcua import Client, ua

class SubHandler(object):
    """
    Subscription Handler class to handle incoming events.
    """
    def event_notification(self, event):
        print("New event received:")
        print("Event Type:", event.EventType)
        print("Severity:", event.Severity)
        print("Message:", event.Message)
        if hasattr(event, 'LocaleIds'):
            print("Locale:", event.LocaleIds)
        print("-" * 20)

def main():
    client = Client("opc.tcp://localhost:4840")  # Replace with your server address
    try:
        client.connect()
        print("Client Connected")

        # Create a subscription 
        sub = client.create_subscription(500, SubHandler())
        
        # Subscribe to Alarm & Condition events
        handle = sub.subscribe_events()

        # Setting LocaleIds to "mul" to receive messages in multiple languages
        params = ua.ReadParameters()
        params.locale_ids = ["mul"]
        client.uaclient.set_attribute(params)

        print("Subscription created, listening for events...")

        try:
            # Keep the script running
            while True:
                pass
        except KeyboardInterrupt:
            print("Received interrupt signal, exiting...")
        
    finally:
        client.disconnect()
        print("Client disconnected")

if __name__ == "__main__":
    main()