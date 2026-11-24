# OPCUA-AC-Client
Command line OPCUA AC Client for testing S7-1500 CPU OPCUA server alarms and controls feature

Wanted to test a specific feature called "Simultaneous receipt of alarms in multiple languages" on a S7-1500 CPU OPCUA server. 

https://docs.tia.siemens.cloud/r/en-us/v21.1/configuring-automation-systems/using-opc-ua-communication-s7-1200-s7-1200-g2-s7-1500-s7-1500t/using-the-s7-1500-as-an-opc-ua-server-s7-1200-g2-s7-1500/providing-alarms-on-the-opc-ua-server-s7-1500/simultaneous-receipt-of-alarms-in-multiple-languages-s7-1500

I did not find and did not have access to any commercially available OPCUA clients that would have this feature developed so I created a command line tool to test this. 

You change the value between the [ ] brakets in 
``` session.default_request_params.locale_ids = ["mul"] ``` to either "mul" or "qst"

To get alarms with all available languages use the "qst" option 

> If no other LocaleIds follow the LocaleId "qst", all available languages are provided by the server.

To run this use command line or powershell, navigate to the folder where this files exist and type 
``` python ./OpcClient.py ```
OR
``` python ./OpcUAClient_Asych.py ```

Example file assume you are running a S7-PLC SIM Advanced instance on the same computer with the TCP/IP Single Adapter functionality on and that PLC is using the default OPCUA port 4840
Update the row ``` url = "opc.tcp://localhost:4840" ``` to match your use case and setup 

