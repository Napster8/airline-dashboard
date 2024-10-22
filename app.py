from taipy import Gui
from pages.overview_page.overview_page import Overview
from pages.marketing_page.marketing_page import Marketing
from data.data_processing import setup_bigquery_client, run_dbt
from navbar import nav_bar # import the Top Navigation Bar

setup_bigquery_client()
#run_dbt()

# Page Structure
pages = {
    "overview": Overview,
    "marketing": Marketing
}

# Create a Gui object
gui = Gui(pages=pages)

if __name__ == "__main__":
    gui.run(title="Airline Dashboard", port=5000, dark_mode=False, use_reloader=True)
