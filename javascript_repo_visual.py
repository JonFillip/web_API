import requests

from plotly.graph_objs import Bar
from plotly import offline

# Call the API and store the response.
url = 'https://api.github.com/search/repositories?q=language:javascript&sort' \
      '=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
response_obj = requests.get(url, headers=headers)
print(f"Status code: {response_obj.status_code}")

# Store the API response in a variable.
response_dict = response_obj.json()
print(f"Total repositories: {response_dict['total_count']}")

# Print the main header keys from the response.
print(response_dict.keys())

# Explore the data keys in the items key.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in repo_dict.keys():
    print(key)
# Extract the necessary values from the result to plot a chart
repo_links, stars, labels, ids = [], [], [], []
for repo_dict in repo_dicts:
    try:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

        star_count = int(repo_dict['stargazers_count'])
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"

    except ValueError:
        print(f"Data not found for repo id {repo_dict['id']}")

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
        'color': 'rgb(100, 150, 250)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.5,
}]

# Create Layout
my_layout = {
    'title': 'Most Popular Javascript Repositories on GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10},
    },
}
fig = {'data': data, 'layout': my_layout}

if __name__ == "__main__":
    offline.plot(fig, filename='/Users/johnphillip/Desktop/web_api/plots'
                               '/js_plot.html')
