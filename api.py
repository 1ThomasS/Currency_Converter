import requests

def get_url(url):

    try:

        response = requests.get(url)
        status_code = response.status_code
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            return status_code, content

        else:
            error_message = f"Error: {status_code} - {response.reason}"
            return status_code, error_message

    except requests.exceptions.RequestException as e:

        return 500, f"Request Exception: {str(e)}"

