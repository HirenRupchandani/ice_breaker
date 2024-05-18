import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(profile_url: str='https://linkedin.com/in/hiren-rupchandani/', un_mock: bool = False):
    """
    scrape information from LinkedIn Profile. Using Proxycurl
    :param profile_url: URL of scraped profile
    :param mock: a boolean
    :return:
    """

    """
    API CALL
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    api_key = 'your_key'
    headers = {'Authorization': 'Bearer ' + api_key}
    params = {'url':'https://linkedin.com/in/hiren-rupchandani/','fallback_to_cache':'on-error','skills':'include','use_cache':'if-recent'}
    response = requests.get(api_endpoint, params=params, headers=headers)
    """

    if un_mock:
        print('here at unmock')
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": profile_url},
            headers=header_dic,
            timeout=10,
        )
    else:
        print('here at mock')
        profile_url = "https://gist.githubusercontent.com/HirenRupchandani/22a28e106c259b8fd054a4449da212b9/raw/ddedfd665eaa2b4de440c69d91b7794d6123abb5/hiren-linkedin.json"
    try:
        response = requests.get(profile_url, timeout=10)
        data = response.json()
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
        }
        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")
        return data
    except requests.exceptions as e:
        print(e)
        return {}


if __name__ == "__main__":
    print(scrape_linkedin_profile())
