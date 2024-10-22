# config.py

from taipy import Config

PROJECT_ID = "airline-438510"
DATASET_ID = "airlines"
DBT_DATASET = f"{PROJECT_ID}.{DATASET_ID}"

# Configure the GUI
Config.configure_gui(
    name="Airline Dashboard",
    description="An overview and marketing dashboard for Airline Firm.",
    author="Raghavendra Tapas",
)

# Configure global application settings
Config.configure_global_app(
    dark_mode=False,
    navigation=True,
)
