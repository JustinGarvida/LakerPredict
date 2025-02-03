from bs4 import BeautifulSoup
import requests
import pandas as pd

def fetch_last_10_games_stats(player_url):
    """
    Fetches the first 10 rows of selected statistics for a player from basketball-reference.com and returns the data as JSON.

    Args:
        player_url (str): The URL of the player's game log page.

    Returns:
        str: A JSON string containing the first 10 rows of selected statistics.
    """
    response = requests.get(player_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'id': 'pgl_basic'})

        if table:
            headers = [th.text for th in table.find('thead').find_all('th')]

            rows = []
            for row in table.find('tbody').find_all('tr', {'id': lambda x: x and x.startswith('pgl_basic.')}):
                row_data = [td.text.strip() for td in row.find_all('td')]
                rows.append(row_data)

            selected_indices = [2, 6, 21, 22, 27]
            selected_stats = [headers[i] for i in selected_indices]

            df = pd.DataFrame(rows, columns=headers[1:])

            df_selected = df[selected_stats]

            # Get the first 10 rows and convert to JSON
            df_first_10_rows = df_selected.head(10)
            json_data = df_first_10_rows.to_json(orient='records')

            return json_data
        else:
            print("Table not found.")
            return "Table not found."
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return f"Failed to retrieve the page. Status code: {response.status_code}"

