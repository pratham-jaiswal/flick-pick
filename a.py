import requests
import re

def check_for_update(githubReleaseURL):
    try:
        response = requests.get(githubReleaseURL)
        if response.status_code == 200:
            pageContent = response.text
            latestVersion = re.search(r"FlickPick v([\d.]+)", pageContent)
            if latestVersion:
                latestVersion = latestVersion.group(1)
                currentVersion = "0.1.0"
                githubLatestURL = f"{githubReleaseURL}tag/v{latestVersion}"
                if latestVersion > currentVersion:
                    if latestVersion[0] > currentVersion[0]:
                        print(githubLatestURL+"    a")
                    else:
                        print(githubLatestURL)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

githubReleaseURL = "https://github.com/pratham-jaiswal/flick-pick/releases/"
check_for_update(githubReleaseURL)