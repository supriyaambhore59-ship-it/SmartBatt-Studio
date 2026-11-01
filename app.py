import streamlit as st

st.set_page_config(
    page_title="SmartBatt Studio",
    page_icon="🔋",
    layout="wide"
)

st.title("🔋 SmartBatt Studio")
st.subheader("Interactive Battery Energy System Calculator")

st.write(
    "Explore battery pack configurations by entering "
    "your actual cell specifications."
)

st.warning(
    "This tool provides preliminary calculations, "
    "not battery safety certification or a validated BMS design."
)

# User inputs
st.sidebar.header("Battery Specifications")

cell_voltage = st.sidebar.number_input(
    "Cell nominal voltage (V)",
    min_value=0.1,
    max_value=10.0,
    value=3.7,
    step=0.1
)

cell_capacity = st.sidebar.number_input(
    "Cell capacity (Ah)",
    min_value=0.1,
    value=2.5,
    step=0.1
)

series = st.sidebar.number_input(
    "Cells in series (S)",
    min_value=1,
    max_value=100,
    value=4,
    step=1
)

parallel = st.sidebar.number_input(
    "Parallel groups (P)",
    min_value=1,
    max_value=100,
    value=2,
    step=1
)

charge_current = st.sidebar.number_input(
    "Charging current (A)",
    min_value=0.1,
    max_value=100.0,
    value=2.0,
    step=0.1
)

# Calculations
pack_voltage = cell_voltage * series
pack_capacity = cell_capacity * parallel
energy_wh = pack_voltage * pack_capacity
total_cells = int(series * parallel)
ideal_charge_hours = pack_capacity / charge_current

# Results
st.header("Calculated Results")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Nominal Pack Voltage", f"{pack_voltage:.2f} V")
c2.metric("Pack Capacity", f"{pack_capacity:.2f} Ah")
c3.metric("Nominal Energy", f"{energy_wh:.2f} Wh")
c4.metric("Total Cells", str(total_cells))

st.subheader("Configuration Summary")

st.success(
    f"Your selected battery configuration is "
    f"{int(series)}S{int(parallel)}P."
)

st.write(f"- Series cells: {int(series)}")
st.write(f"- Parallel groups: {int(parallel)}")
st.write(f"- Total cells: {total_cells}")
st.write(f"- Nominal energy: {energy_wh / 1000:.3f} kWh")

st.subheader("Ideal Charging-Time Estimate")

st.metric("Ideal Time", f"{ideal_charge_hours:.2f} hours")

st.caption(
    "This estimate uses capacity divided by charging current. "
    "Actual charging time varies with charging stages, battery "
    "chemistry, temperature, losses, and BMS limits. "
    "Use only charging currents approved for your battery."
)

# Energy visualization
st.subheader("Energy Overview")

st.bar_chart({
    "Energy (Wh)": {"Battery pack": energy_wh}
})

st.info(
    "Nominal energy is estimated from nominal voltage × capacity. "
    "Actual usable energy depends on operating limits and losses."
)
