from bs4 import BeautifulSoup
import requests
import pandas as pd

def fetch_last_10_games_stats(player_url):
    """
    Fetches the first 10 rows of selected statistics for a player from basketball-reference.com.

    Args:
        player_url (str): The URL of the player's game log page.

    Returns:
        pd.DataFrame: A DataFrame containing the first 10 rows of selected statistics.
    """
    # Fetch the webpage content
    response = requests.get(player_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the id 'pgl_basic'
        table = soup.find('table', {'id': 'pgl_basic'})

        if table:
            # Extract the headers
            headers = [th.text for th in table.find('thead').find_all('th')]

            # Extract the rows
            rows = []
            for row in table.find('tbody').find_all('tr', {'id': lambda x: x and x.startswith('pgl_basic.')}):
                row_data = [td.text.strip() for td in row.find_all('td')]
                rows.append(row_data)

            # Define selected stats by indices
            selected_indices = [2, 6, 21, 22, 27]
            selected_stats = [headers[i] for i in selected_indices]

            # Convert to DataFrame with full headers
            df = pd.DataFrame(rows, columns=headers[1:])

            # Select only the columns of interest
            df_selected = df[selected_stats]

            # Get the first 10 rows
            df_first_10_rows = df_selected.head(10)

            return df_first_10_rows
        else:
            print("Table not found.")
            return pd.DataFrame()
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return pd.DataFrame()

