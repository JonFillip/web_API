import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
response_obj = requests.get(url, headers=headers)
print(f"Status code: {response_obj.status_code}")

# Store API response in a variable.
response_dict = response_obj.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process results main header keys.
# print(response_dict.keys())

# Explore the information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#    print(key)
print("\nSelected information about the each repository returned:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository address: {repo_dict['html_url']}")
    print(f"Date of creation: {repo_dict['created_at']}")
    print(f"Last updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
