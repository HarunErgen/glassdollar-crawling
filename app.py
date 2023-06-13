from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/corporate_details")

@app.get("/corporate_details")
async def get_corporate_details():
    url = "https://ranking.glassdollar.com/graphql"

    cookies = {
        'fpestid': 'dBDZarTIK5_YJ9xmXLs-d8Xd8vEm14VnsuDsrkYDXskuQKZBLKMamm229xPCvOR1h3ugzw',
        '_gid': 'GA1.2.1426872978.1686671112',
        'pubconsent-v2': 'YAAAAAAAAAAA',
        'euconsent-v2': 'CPtTO8APtTO8AAZACBENDICsAP_AAH_AAAAAJftX_H__bW9r8f7_aft0eY1P9_j77uQzDhfNk-4F3L_W_JwX52E7NF36tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5umxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eX33_79_7_H9-f_876CXYBJhq3EAXYlDgTaBhFCiBGFYQEUCgAgoBhaICABwcFOyMAn1hEgBQCgCMCIEOAKMiAQAAAQBIRABIEWCAAAAQCAAEACARCAAgYBBQAWAgEAAIDoGKIUAAgSECREREKYEBECQQEtlQglBdIaYQBVlgBQCI2CgARAACKwABAWDgGCJASsWCBJiDaIABgBQCiVCtQSemgAWMjYAA.YAAAAAAAAAAA',
        '_ga': 'GA1.2.1601954358.1686671111',
        '_ga_SX8XLCG27H': 'GS1.1.1686676570.2.1.1686681278.0.0.0',
    }

    headers = {
        'authority': 'ranking.glassdollar.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://ranking.glassdollar.com',
        'referer': 'https://ranking.glassdollar.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
    }

    top_ranked_corporates_json_data = {
        "operationName": "GetTopRankedCorporates",
        "variables": {},
        "query": "query GetTopRankedCorporates {\n  topRankedCorporates {\n    id\n  }\n}\n"
    }

    top_ranked_corporates_response = requests.post(url, cookies=cookies, headers=headers, json=top_ranked_corporates_json_data)
    top_ranked_corporates_response_data = top_ranked_corporates_response.json()


    # add corporates data into corporate details
    result_json = {
        'corporate_details':[]
    }
    for corporate in top_ranked_corporates_response_data['data']['topRankedCorporates']:
        corporate_id = corporate['id']

        corporate_details_json_data = {
            "operationName": "GetCorporateDetails",
            "variables": {
                "id": corporate_id
            },
            "query": "query GetCorporateDetails($id: String) {\n  corporate(id: $id) {\n    name\n    description\n    logo_url\n    hq_city\n    hq_country\n    website_url\n    linkedin_url\n    twitter_url\n        startup_partners_count\n    startup_partners {\n      company_name\n      logo\n      city\n      website\n      country\n      theme_gd\n    }\n    startup_themes\n  }\n}\n"
        }

        corporate_details_response = requests.post(url, json=corporate_details_json_data)
        corporate_details_response_data = corporate_details_response.json()
        
        result_json['corporate_details'].append(corporate_details_response_data['data']['corporate'])

    return result_json
