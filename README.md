# pco-python-sdk
A Python SDK for simplifying interactions with the Planning Center API.


## NOTE: WIP. This library is not stable and is under active development. I will release a 1.x.x version when the library has reached a stable state.

## Currently only supporting the latest version of all the APIs. Will come up with a better versioning strategy after 1.0

## Need to install
poetry
python
ruff
pre-commit

## NOTE: Not currently supporting the json fields in the attribute payloads

# Getting Started

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install pco_python_sdk
```

## Contributing

This project is under active development. Feel free to contribute and submit a pull request. The project is managed with poetry and tests use pytest.

# Docs

## Webhooks

You can validate a webhook using the `WebhookSignature` class. Pass the request headers, the body of the request, and the secret to `.verify` which will return `True/False` depending if the signature is verified. A `SignatureVerificationError` will be raise for any exceptions.
