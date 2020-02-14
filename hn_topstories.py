from operator import itemgetter

import requests
from plotly import offline

# Call the API and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
response_obj = requests.get(url)
print(f"Status code: {response_obj.status_code}")

# Process the information about the submission
submission_ids = response_obj.json()
submission_dicts = []
for submission_id in submission_ids[:20]:
    # Make a separate call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/' \
          f'item/{submission_id}.json?print=pretty'
    response = requests.get(url)
    print(f"id: {submission_id}\tStatus:{response.status_code}")
    response_dict = response.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Create lists to collect data points for the plot.
titles, story_links, comments = [], [], []
for submission in submission_dicts:
    try:
        title = submission['title']
        comment = submission['comments']
        news_link = submission['hn_link']

        disc_link = f"<a href='{news_link}'>{title[:20]}</a>"

    except ValueError:
        continue

    else:
        story_links.append(disc_link)
        titles.append(title)
        comments.append(comment)

# Create and style visualization
data = [{
    'type': 'bar',
    'x': story_links,
    'y': comments,
    'hovertext': titles,
    'marker': {
        'color': 'goldenrod',
        'line': {'width': 1.5, 'color': 'grey'}
    },
    'opacity': 0.6,
}]

# Create layout
my_layout = {
    'title': 'Most Popular News Stories on Hacker-News',
    'xaxis': {
        'title': 'Story Titles',
        'titlefont': {
            'size': 20
        },
        'tickfont': {'size': 15},
    },
    'yaxis': {
        'title': 'Engagement/Comments',
        'titlefont': {'size': 20},
        'tickfont': {'size': 15}
    },
}

fig = {'data': data, 'layout': my_layout}

if __name__ == "__main__":
    offline.plot(fig, filename='/Users/johnphillip/Desktop/web_api/plots'
                               '/hn_visualization.html')
