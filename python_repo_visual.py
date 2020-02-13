import requests
from plotly import offline

# Call the git API and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
header = {'Accept': 'application/vnd.github.v3+json'}
# Get the response object passing the url and header parameters into a get
# function and print a status code to see if our call was successful.
response_obj = requests.get(url, headers=header)
print(f"Status code: {response_obj.status_code}")

# Store the API response in a variable
response_dict = response_obj.json()
print(f"Total repositories: {response_dict['total_count']}")

# Print the main header keys from the response
print(response_dict.keys())

# Explore the data about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Process the results
repo_links, stars, labels = [], [], []
for repo in repo_dicts:
    try:
        repo_name = repo['name']
        repo_url = repo['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

        star_count = int(repo['stargazers_count'])
        owner = repo['owner']['login']
        description = repo['description']
        label = f"{owner}<br />{description}"

    except ValueError:
        print(f"Data not found for {repo['name']}")

    else:
        repo_links.append(repo_link)
        stars.append(star_count)
        labels.append(label)

# Create and style visualization
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(116,173,209)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
# Create Layout
my_layout = {
    'title': "Most popular Python Projects on GitHub",
    'xaxis': {
        'title': "Repository",
        'titlefont': {'size': 20},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 20},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}

if __name__ == '__main__':
    offline.plot(fig, filename='/plots/python_repo.html')
