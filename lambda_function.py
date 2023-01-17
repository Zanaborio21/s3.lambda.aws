import json
import os
import mercadopago

    

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    body=json.loads(event["body"])
    
    
    payment_response = sdk.payment().create(body)
    payment = payment_response["response"]
    json_payment=json.dumps(payment_response['response'])
    

    print(payment)
    print(json_payment)

    return {
        "statusCode": 200,
        "body": json.dumps(payment),
    }
