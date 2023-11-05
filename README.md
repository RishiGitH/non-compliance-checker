# non-compliance-checker

## Prerequisites

- Python 3.8.9
- Pipenv

## Environment Setup

1. Ensure you have python3.x installed on your machine. You can check your python version using:

```bash
$ python --version
```

2. Install Pipenv if you don't have it. 

```bash
$ pip install pipenv
```

## Project Setup

1. Clone this git repository to your local machine.

```bash
$ git clone https://github.com/RishiGitH/non-compliance-checker.git
```

2. Change directory into the project folder:

```bash
$ cd non-compliance-checker
```

3. Install the project dependencies:

```bash
$ pipenv install
```

4. Activate the Pipenv shell:

```bash
$ pipenv shell
```

5. Once you have activated the Pipenv shell, you should now be able to run the Django server:

```bash
$ python manage.py runserver
```

6. Create .env file and update it with OPENAI_API_KEY or run below command
```bash
export OPENAI_API_KEY=sk-your-key
```



## Sample Success Response Image
![Alt text](readme_images/response.png?raw=true "Success Response")

### Sample Error Responses
![Alt text](readme_images/error2.png?raw=true "Missing Fields Error")

![Alt text](readme_images/error1.png?raw=true "Unexpected Error")




### Sample Curl Request
curl --request GET \
  --url 'http://127.0.0.1:8000/complianceCheck?webpage_url=https%3A%2F%2Fwww.joinguava.com%2F&compliance_policy_url=https%3A%2F%2Fstripe.com%2Fdocs%2Ftreasury%2Fmarketing-treasury'

### Sample Success Response 

```json
[
	{
		"compliance_issue": "Use of prohibited terms",
		"description": "The website uses the terms 'banking', 'business checking account', and 'virtual debit card', which are prohibited by the compliance policy as they can draw scrutiny from regulators."
	},
	{
		"compliance_issue": "Misrepresentation of FDIC insurance",
		"description": "The website claims to offer FDIC insurance eligibility without providing the required disclosures specified in the compliance policy."
	},
	{
		"compliance_issue": "Inaccurate description of Stripe Treasury balances",
		"description": "The website refers to the balances as 'stored value accounts', which is an imprecise terminology and may draw scrutiny from regulators."
	},
	{
		"compliance_issue": "Failure to comply with recommended terms",
		"description": "The website does not use the recommended terms provided in the compliance policy when describing the product."
	},
	{
		"compliance_issue": "Misleading statement about being a banking platform",
		"description": "The website claims to be 'not just a banking platform' but offers services similar to traditional banking, which may mislead customers about the nature of the product."
	}
]
```