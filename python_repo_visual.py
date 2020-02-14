import requests
from plotly import offline


# Call the git API and store the response
def get_response():
    """Make an API call and return the response"""
    url = 'https://api.github.com/search/repositories?q=language:python&sort' \
          '=stars'
    header = {'Accept': 'application/vnd.github.v3+json'}
    # Get the response object passing the url and header parameters into a get
    # function and print a status code to see if our call was successful.
    resp_obj = requests.get(url, headers=header)
    return resp_obj


def get_repo_dicts():
    """Get and store the repo dict keys from the response."""
    response_dict = response_obj.json()
    print(f"Total repositories: {response_dict['total_count']}")

    # Explore the data about the repositories
    repo_dictionaries = response_dict['items']

    return repo_dictionaries


def get_repo_data():
    """Examine and return data points in a list for visualization."""
    repos_links, num_stars, label_s = [], [], []
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
            repos_links.append(repo_link)
            num_stars.append(star_count)
            label_s.append(label)

    return repos_links, num_stars, label_s


def plot_graph():
    """Make visualization for derived data"""
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
    offline.plot(fig, filename='/Users/johnphillip/Desktop/web_api/plots'
                               '/python_repo.html')


if __name__ == '__main__':
    response_obj = get_response()
    repo_dicts = get_repo_dicts()
    repo_links, stars, labels = get_repo_data()
    plot_graph()
