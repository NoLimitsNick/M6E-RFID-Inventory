import mercury,boto3,botocore, json
reader = mercury.Reader("tmr:///dev/ttyUSB0")

print("Starting RFID Single Read Script...");
reader.set_region("NA2")
reader.set_read_plan([1],"GEN2",bank=["user","epc","tid"])
reader.set_read_powers([1],[500])

readTag = reader.read();
apc_code=str(readTag[0]);
apc = apc_code[2:26]
print("The tag being read is:",apc)

lambda_client = boto3.client('lambda')
test_event = {
  "Container_Code": apc
}
testData = json.dumps(test_event)

response = lambda_client.invoke(
  FunctionName='RegisterTag',
  InvocationType='RequestResponse',
  Payload=testData,
)
if (response['StatusCode'] == 200):
	print('Registered Tag: ',apc);
else:
	print("Error Sending Tag Information");
