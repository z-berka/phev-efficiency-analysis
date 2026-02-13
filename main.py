from src.load_data import load_dataset
from src.energy_analysis import (
    compute_fuel_energy,
    compute_total_energy,
    compute_specific_energy,
)
from src.efficiency_models import estimate_drivetrain_efficiency
from src.visualization import (
    plot_energy_vs_speed,
    plot_urban_share_effect,
)

DATA_PATH = "data/JRC_Dataset_PHEV_test_campaign_20240920.xlsx"


def run_pipeline():
    print("Loading dataset...")
    df = load_dataset(DATA_PATH)

    print("Computing fuel energy...")
    df = compute_fuel_energy(df)

    print("Computing total energy input...")
    df = compute_total_energy(df)

    print("Computing specific energy consumption...")
    df = compute_specific_energy(df)

    print("Estimating drivetrain efficiency...")
    df = estimate_drivetrain_efficiency(df)

    print("Generating plots...")
    plot_energy_vs_speed(df)
    plot_urban_share_effect(df)

    print("Analysis complete.")
    return df


if __name__ == "__main__":
    run_pipeline()
