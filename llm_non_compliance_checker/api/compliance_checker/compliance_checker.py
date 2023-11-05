import json
from api.scrapper.web_scrapper import WebScraper
from api.llm_apis.openai_api import OpenAIAPI



class ComplianceChecker:
    def __init__(self, policy_url, web_page_url):
        self.policy_url = policy_url
        self.web_page_url = web_page_url
        self.user_custom_prompt = ("Now based on the given compliance policy and "
        "the scraped text data of the website. Check what all non compliance issues "
        "are there with the website. Check the content in the page against the "
        "compliance policy. Return the findings (non-compliant results) in a short, "
        "concise easy to understand and return in the form of a json list.  "
        'Always return the output in this format of json list '
        '["compliance_issue": "issue headline", description":"write description here"]'
        "Only use the compliance text and website text don't assume anything "
        "on your own. Try to find as many non-compliant results as you can")


    @staticmethod
    def get_scraped_data(url):
    	# scrapping web page
        scraper = WebScraper(url)
       	return scraper.extract_paragraphs()

    def package_data_in_messages_list_form(self, scraped_policy_data, scraped_web_page_data):
        messages = [
        {"role": "system", "content": "This is a compliance policy data \n {} This is this is"\
        " a scraped text data  from a web page {} ".format(scraped_policy_data,scraped_web_page_data)
        },
        {"role": "user", "content": self.user_custom_prompt}]
        return messages

    def beautify_api_response(self, api_response):
        return json.loads(api_response)



    def find_non_compliance_results(self):
        policy_data = ComplianceChecker.get_scraped_data(self.policy_url)
        web_page_data = ComplianceChecker.get_scraped_data(self.web_page_url)
        messages_data = self.package_data_in_messages_list_form(
            scraped_policy_data=policy_data,scraped_web_page_data=web_page_data)
        api_response = OpenAIAPI().get_response(messages_data)

        return self.beautify_api_response(api_response)
