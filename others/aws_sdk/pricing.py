aws_creds = {
    'aws_access_key_id': '',
    'aws_secret_access_key': ''
}

import boto3

# Billing Conductor
billingConductorClient = boto3.client('billingconductor')
print(billingConductorClient)

# Get the current bill of AWS account using Cost Explorer API
costExplorerClient = boto3.client('ce')
data = costExplorerClient.get_cost_and_usage(
    TimePeriod={
        'Start': '2024-01-01',
        'End': '2024-01-30'
    },
    Granularity='DAILY',
    Metrics=['BlendedCost']
)
print(len(data['ResultsByTime']))

# Get AWS services price list
priceClient = boto3.client('pricing')
print(priceClient)
