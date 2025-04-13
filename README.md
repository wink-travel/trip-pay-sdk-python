[![trippay.io logo](https://res.cloudinary.com/traveliko/image/upload/c_scale,h_75/v1632220708/trippay/brand/TP_logo_v2_PURPLE_trans.png)](https://trippay.io)

# TripPay Python SDK

Welcome to the Python SDK that enables you to communicate with all that the TripPay platform has to offer.

## Getting started
This SDK contains libraries you can leverage to communicate with the TripPay platform.

### Python Requirements
Python 3.8+

Download libraries from PyPi.

## Payment

[API documentation](trip-pay-sdk-payment/README.md)

The Payment API exposes endpoints for affiliates and hotels to track bookings, analytics and funds availability. They can also choose to withdraw available funds to their bank account.

#### API's

- AccountApi: Manage your account(s) on Wink with the Account API.
- AccountMappingsApi: Manage your account mappings on Wink with the Account Mapping API.
- AgentApi: Create a booking contract as an Agent with the Agent API.
- ApplicationApi: Manage your applications.
- ContractApi: Retrieve booking contracts and cancel them if possible.
- ManagingEntityApi: Managed entities can be bound to applications and webhooks..
- MappingApi: More mapping features to control mappings between your system and Wink.
- PingApi: Easy way to check if you are connected and authenticated with the Wink platform.
- WebhookApi: Use the Webhook API to create webhooks to interface with the TripPay API.

#### How to install

[PyPi URL](https://pypi.org/project/trip-pay-sdk-payment)

You can install the package from PyPi using:
```sh
pip install trip_pay_sdk_payment
```



## Configuration
You will need a client ID and a client secret to communicate with any of the Wink platform endpoints. You can create your account and get your credentials here:

[https://sell.wink.travel](https://sell.wink.travel)

Steps: 
1. Register your personal user account
2. Log in
3. Create your first account
4. Select that account
5. Choose to create an Application for that account 
6. The application will hold your credentials

Using the client ID and client secret, you can create the OAUTH2 access token. Instructions to create the access token you can find in the API docs Authentication section, eg.
[https://docs.wink.travel/affiliate](https://docs.wink.travel/affiliate)


### ENV variables
Create the access token environment variable in your preferred way:

1. ACCESS_TOKEN=YOUR_ACCESS_TOKEN


## You might also be interested in...

- Wink Python SDK Repo: [https://github.com/wink-travel/wink-sdk-python](https://github.com/wink-travel/wink-sdk-python)
- WordPress: [https://wordpress.org/plugins/wink2travel/](https://wordpress.org/plugins/wink2travel/)
