from operator import itemgetter
import requests

# Call the API and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
response_obj = requests.get(url)
print(f"Status code: {response_obj.status_code}")

# Process the information about the submission
submission_ids = response_obj.json()
submission_dicts = []
for submission_id in submission_ids[10: 20]:
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
