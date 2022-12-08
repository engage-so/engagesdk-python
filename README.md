# Engage Python SDK

The Engage Python SDK lets you capture user attributes and events on your site. You can later use this on Engage to create user segments for analytics, broadcast messages and automation messages.

## Getting Started

[Create an Engage account](https://engage.so/) to get your API key


## Installation

```ssh
pip install engagesdk
```

## Configuration

Initialise the SDK with your public and private key. Your keys are available in the settings page of your Engage dashboard.

```python
from engagesdk import Engage

engage = Engage(api_key = '', secret_key = '')

```

## Identifying users

You only need a unique identifier that represents the user on your platform to track their events and attributes on Engage. To correlate a proper profile to these tracked attributes and events, you can send the unique identifier and other properties to Engage. You only need to do this once per user, probably at user signup. 

```python
engage.users.identify({
  'id': 'u13345',
  'email': 'dan@mail.app',
  'created_at': '2020-05-30T09:30:10Z'
})
```

`id` represents the unique identifier for the user on your platform. It is the only required parameter. You can send any other attribute you want e.g. `age`, `plan`. Here are the standard ones we use internally on the user profile:
- `first_name`
- `last_name`
- `email`
- `is_account`
- `number` (with international dialing code without the +)
- `created_at` (represents when the user registered on your platform. If not added, Engage sets it to the current timestamp.)
- `device_platform`
- `device_token`


## Update/add user attributes

If you need to add new attributes or update an existing attribute, you can use the `add_attribute` method. 

```python
engage.users.add_attribute(user_id, {
  'first_name': 'Dan',
  'plan': 'Premium'
})
```

(You can also use `identify` to update or add new attributes.)

## Tracking user events and actions

You can track user events and actions in a couple of ways. 

Tracking an event with no value:

```python
engage.users.track(user_id, 'paid');
```

Tracking an event with a value:

```python
engage.users.track(user_id, {
  'event': 'New badge',
  'value': 'gold',
  'timestamp': '2020-05-30T09:30:10Z'
})
```

`event` is the event you want to track. `value` is the value of the event. This can be a string, number or boolean. There is an optional `timestamp` parameter. If not included, Engage uses the current timestamp. The timestamp value must be a valid datetime string.

If you need to track more properties with the event, you can track it this way:

```python
engage.users.track(user_id, {
  'event': 'Add to cart',
  'properties': {
    'product': 'T123',
    'currency': 'USD',
    'amount': 12.99
  }
})
```

## Convert User to Account

Converts a Customer to Account

```python
engage.users.convert_to_account(user_id)
```

## Convert User to Customer

Converts a Customer to Customer

```python
engage.users.convert_to_customer(user_id)
```

## Add user to an account

This adds a user to an account if it exists

```python
engage.users.add_to_account(user_id= "uid", account_id= "aid", role="developer")
```

## Change a user's role in an account

This changes a user's role in an account

```python
engage.users.change_account_role(user_id= "uid", account_id= "aid", role="admin")
```

## Remove a user from an account

This removes a user from an account

```python
engage.users.remove_from_account(user_id= "uid", account_id= "aid")
```

## License

MIT
