import plotly.express as px
import pandas as pd

def bar_skill_match(matched: dict) -> 'plotly.graph_objs._figure.Figure':
    df = pd.DataFrame({
        "Skill": list(matched.keys()),
        "Match": list(matched.values())
    })
    fig = px.bar(df, x="Skill", y="Match", title="Skill Match (1=present, 0=missing)")
    return fig

def gauge_score(score: float) -> 'plotly.graph_objs._figure.Figure':
    # Simple workaround using bar to represent a gauge-like view
    df = pd.DataFrame({"Metric": ["Overall Score"], "Score": [round(score*100, 2)]})
    fig = px.bar(df, x="Metric", y="Score", range_y=[0, 100], title="Overall Match %")
    return fig