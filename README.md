## Quick Start

- [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
- [Enable billing for your project](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).
- [Enable the Google Cloud APIs](https://cloud.google.com/apis/docs/getting-started).
- [Setup Authentication](https://googleapis.dev/python/google-api-core/latest/auth.html).

## System requirements
* Operating systems:
    * Linux
    * Mac OS X
    * Windows
* [Python 2.7, or 3.4 or higher](http://python.org/download/)

## Installing virtualenv

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

## Installing the client library

* `pip`
```
$ pip install --upgrade google-api-python-client
```

* `setuptools`
```
$ easy_install --upgrade google-api-python-client
```

* Manual installation
Download the latest [client library for Python](https://pypi.org/project/google-api-python-client/), unpack the code, and run python setup.py install 

```
