import requests
import pandas as pd

# Replace with your Monday API token
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYzMTAwNzg2NiwiYWFpIjoxMSwidWlkIjoxMDA4MTI5NzAsImlhZCI6IjIwMjYtMDMtMTBUMDU6NTQ6MzIuNzU5WiIsInBlciI6Im1lOndyaXRlIiwiYWN0aWQiOjM0MTUzNDA5LCJyZ24iOiJhcHNlMiJ9.eXCxujehvur83mye1hEeOtetjLkfYjm6lPpny3cZiHo"

url = "https://api.monday.com/v2"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}


def get_board_items(board_id):
    """
    Fetch all items from a Monday.com board and convert them into a pandas DataFrame
    """

    query = """
    query ($board_id: [ID!]) {
      boards(ids: $board_id) {
        items_page(limit: 100) {
          items {
            name
            column_values {
              column {
                title
              }
              text
            }
          }
        }
      }
    }
    """

    try:
        response = requests.post(
            url,
            json={
                "query": query,
                "variables": {"board_id": int(board_id)}
            },
            headers=headers
        )

        data = response.json()

        # Debug print if API fails
        if "data" not in data:
            print("API Error:", data)
            return pd.DataFrame()

        boards = data["data"]["boards"]

        if not boards:
            print("No boards found.")
            return pd.DataFrame()

        items = boards[0]["items_page"]["items"]

        records = []

        for item in items:

            row = {"Item Name": item["name"]}

            for col in item["column_values"]:
                title = col["column"]["title"]
                value = col["text"]

                row[title] = value

            records.append(row)

        df = pd.DataFrame(records)

        return df

    except Exception as e:
        print("Error fetching board data:", e)
        return pd.DataFrame()