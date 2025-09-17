import streamlit as st
import pandas as pd
import numpy as np

import treat_sim.model as md  # Scenario + runners

TITLE = "Create custom experiments"
INFO_3 = "### Upload custom scenarios and compare results."
INFO_4 = "> Notes: values are interpreted as relative changes to parameters. "
INFO_5 = "Resource and service times are bounded at 0."
PARAM_TXT = "txt/import_data.md"
EXECUTE_TXT = "Execute custom experiments"

# ---------- helpers ----------

def scenario_param_columns():
    """
    Derive editable Scenario attributes from md.Scenario().
    """
    s = md.Scenario()
    # exclude simpy resources created at runtime
    excluded = {
    "arrivals", "seeds",
    "triage", "registration", "exam", "trauma", "cubicle_1", "cubicle_2",
    "lambda_max",          # arrivals for thinning algorithm
    "random_number_set"  # used only for reproducibility
}
    cols = []
    for k, v in vars(s).items():
        if k.startswith("_") or k in excluded:
            continue
        if isinstance(v, (int, float, np.integer, np.floating)) or v is None:
            cols.append(k)
    # stable, readable order
    priority = [
        "n_triage","n_reg","n_exam","n_trauma","n_cubicles_1","n_cubicles_2",
        "triage_mean","reg_mean","reg_var","exam_mean","exam_var","exam_min",
        "trauma_mean","trauma_treat_mean","trauma_treat_var",
        "non_trauma_treat_mean","non_trauma_treat_var","non_trauma_treat_p",
        "prob_trauma",
    ]
    ordered = [k for k in priority if k in cols]
    ordered += [k for k in cols if k not in ordered]
    return ordered

def build_template_df(include_examples: bool = True) -> pd.DataFrame:
    cols = scenario_param_columns()
    if not include_examples:
        return pd.DataFrame(columns=["id", "name"] + cols)

    # example rows (all others default to zero change)
    ex1 = {"id": 1, "name": "exam+1", **{c: 0 for c in cols}}
    if "n_exam" in cols: ex1["n_exam"] = 1

    ex2 = {"id": 2, "name": "short_exam", **{c: 0 for c in cols}}
    if "exam_mean" in cols: ex2["exam_mean"] = -4.0

    ex3 = {"id": 3, "name": "treat+1", **{c: 0 for c in cols}}
    if "n_cubicles_1" in cols: ex3["n_cubicles_1"] = 1

    return pd.DataFrame([ex1, ex2, ex3], columns=["id", "name"] + cols)

def convert_df_to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")

def validate_uploaded(df: pd.DataFrame):
    required = {"id","name"}
    if not required.issubset(df.columns):
        missing = required - set(df.columns)
        return False, f"Missing required columns: {', '.join(missing)}"
    known = set(["id","name"] + scenario_param_columns())
    unknown = [c for c in df.columns if c not in known]
    if unknown:
        return False, "Unknown column(s): " + ", ".join(unknown)
    return True, "OK"
    
# ------------------- field groupings -------------------
CAPACITY_FIELDS = [
    "n_triage", "n_reg", "n_exam", "n_trauma", "n_cubicles_1", "n_cubicles_2"
]

TIME_FIELDS = [
    "triage_mean", "reg_mean", "reg_var", "exam_mean", "exam_var", "exam_min",
    "trauma_mean", "trauma_treat_mean", "trauma_treat_var",
    "non_trauma_treat_mean", "non_trauma_treat_var"
]

PROB_FIELDS = [
    "non_trauma_treat_p", "prob_trauma"
]

# Convenience if you still need a master list of editable fields
VALID_FIELDS = set(CAPACITY_FIELDS + TIME_FIELDS + PROB_FIELDS)


def enforce_bounds(sc, warn_fn=None):
    """
    Ensure scenario parameters are within valid ranges.

    Parameters
    ----------
    sc : Scenario
        The scenario instance to correct in-place.
    warn_fn : callable or None
        Optional function for warnings (e.g. st.warning).
        Called as warn_fn(message) if a correction is made.

    Returns
    -------
    Scenario
        The corrected scenario.
    """
    # capacity counts (must be integers ≥ 0)
    for k in CAPACITY_FIELDS:
        v = getattr(sc, k)
        new_v = max(0, int(round(v)))
        if warn_fn and new_v != v:
            warn_fn(f"{k}: adjusted from {v} to {new_v}")
        setattr(sc, k, new_v)

    # service times and variances (floats ≥ 0)
    for k in TIME_FIELDS:
        v = getattr(sc, k)
        new_v = max(0.0, float(v))
        if warn_fn and new_v != v:
            warn_fn(f"{k}: adjusted from {v} to {new_v}")
        setattr(sc, k, new_v)

    # probabilities (floats between 0 and 1)
    for k in PROB_FIELDS:
        v = getattr(sc, k)
        new_v = min(1.0, max(0.0, float(v)))
        if warn_fn and new_v != v:
            warn_fn(f"{k}: adjusted from {v} to {new_v}")
        setattr(sc, k, new_v)

    return sc


def create_scenarios(df: pd.DataFrame):
    """
    Build dict[name -> Scenario] applying relative deltas, with warnings if inputs are out of range or unknown.
    """
    scenarios = {}
    for _, row in df.iterrows():
        sc = md.Scenario()
        for var_name in df.columns.tolist()[2:]:
            if var_name not in VALID_FIELDS:
                continue
            delta = 0 if pd.isna(row[var_name]) else row[var_name]
            base = getattr(sc, var_name)
            base = 0 if base is None else base
            new_val = base + delta
            setattr(sc, var_name, new_val)
        sc = enforce_bounds(sc)  # clamps to safe values
        scenarios[str(row["name"])] = sc
    return scenarios



def run_experiments(scenarios, n_reps: int):
    return md.run_scenario_analysis(
        scenarios, md.DEFAULT_RESULTS_COLLECTION_PERIOD, n_reps
    )

def results_as_summary_frame(results_dict: dict) -> pd.DataFrame:
    return md.scenario_summary_frame(results_dict).round(1)

# ---------- UI ----------

st.title(TITLE)
st.markdown(INFO_3)

with st.expander("Download template", expanded=True):
    include_examples = st.checkbox("Include example scenarios", value=True)
    template_df = build_template_df(include_examples)
    st.dataframe(template_df, use_container_width=True)
    st.download_button(
        "Download CSV template",
        data=convert_df_to_csv_bytes(template_df),
        file_name="custom_scenarios_template.csv",
        mime="text/csv",
        key="download-template",
    )

st.divider()

uploaded = st.file_uploader("Upload your scenarios CSV", type=["csv"])
if uploaded is not None:
    df_scen = pd.read_csv(uploaded)
    ok, msg = validate_uploaded(df_scen)
    if not ok:
        st.error(msg)
        st.stop()

    st.write("**Loaded experiments**")
    st.dataframe(df_scen, use_container_width=True)
    st.markdown(INFO_4 + INFO_5)

    n_reps = st.slider("Replications", 3, 30, 5, step=1)

    if st.button(EXECUTE_TXT, type="primary"):
        with st.spinner("Running scenario analysis"):
            scenarios = create_scenarios(df_scen)
            results = run_experiments(scenarios, n_reps)
            df_summary = results_as_summary_frame(results)

        st.success("Done!")
        st.subheader("Results (means across replications)")
        st.table(df_summary)

        st.download_button(
            "Download results as CSV",
            data=convert_df_to_csv_bytes(df_summary),
            file_name="experiment_results.csv",
            mime="text/csv",
            key="download-results",
        )
        
st.markdown(open(PARAM_TEXT, encoding="utf-8").read())
       

