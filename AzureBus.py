from azure.servicebus import ServiceBusService, Message, Queue
#c-types


bus_service = ServiceBusService(
    service_namespace='SimplyPaper',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='1Y4YNh7uQ/buNi1v3xunn6F6vfSsJ5+nrmiwKY2WM04')
    
#Endpoint=sb://simplypaper.servicebus.windows.net/;
#SharedAccessKeyName=RootManageSharedAccessKey;
#SharedAccessKey=1Y4YNh7uQ/buNi1v3xunn6F6vfSsJ5+nrmiwKY2WM04=
    
bus_service.create_queue('taskqueue')

queue_options = Queue()
queue_options.max_size_in_megabytes = '5120'
queue_options.default_message_time_to_live = 'PT1M'

bus_service.create_queue('taskqueue', queue_options)

msg = Message(b'Test Message Simply Papaer')
bus_service.send_queue_message('taskqueue', msg)

msg = bus_service.receive_queue_message('taskqueue', peek_lock=False)
print(msg.body)