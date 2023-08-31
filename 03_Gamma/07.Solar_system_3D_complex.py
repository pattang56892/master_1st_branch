import plotly.graph_objects as go
import numpy as np

# Define the data for the planets
planets = {
    "Mercury": {"distance": 0.39, "radius": 0.038, "color": "gray"},
    "Venus": {"distance": 0.72, "radius": 0.095, "color": "bisque"},
    "Earth": {"distance": 1, "radius": 0.1, "color": "mediumturquoise"},
    "Mars": {"distance": 1.52, "radius": 0.053, "color": "indianred"},
    "Jupiter": {"distance": 5.20, "radius": 1.12, "color": "burlywood"},
    "Saturn": {"distance": 9.58, "radius": 0.945, "color": "khaki"},
    "Uranus": {"distance": 19.18, "radius": 0.401, "color": "lightskyblue"},
    "Neptune": {"distance": 30.07, "radius": 0.388, "color": "dodgerblue"}
}

# Create empty lists for the planet coordinates
x_coords = []
y_coords = []
z_coords = []
planet_names = []

# Generate coordinates for each planet
for planet, data in planets.items():
    distance = data["distance"]
    radius = data["radius"]
    color = data["color"]

    theta = 2 * np.pi * np.random.rand(100)
    phi = np.linspace(0, 2 * np.pi, 100)

    x = distance * np.outer(np.cos(phi), np.sin(theta))
    y = distance * np.outer(np.sin(phi), np.sin(theta))
    z = distance * np.outer(np.ones_like(phi), np.cos(theta))

    x_coords.append(x)
    y_coords.append(y)
    z_coords.append(z)
    planet_names.append(planet)

# Create the plot
fig = go.Figure(data=go.Scatter3d(
    x=np.concatenate(x_coords),
    y=np.concatenate(y_coords),
    z=np.concatenate(z_coords),
    mode='lines',
    line=dict(color='gray', width=0.5),
    hoverinfo='none'
))

# Add planet markers
for x, y, z, name in zip(x_coords, y_coords, z_coords, planet_names):
    fig.add_trace(go.Scatter3d(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        mode='markers',
        marker=dict(
            color=planets[name]["color"],
            size=2,
            opacity=0.6
        ),
        name=name
    ))

# Set layout and show the plot
fig.update_layout(
    scene=dict(
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=False, visible=False),
        zaxis=dict(showgrid=False, visible=False),
        aspectmode="manual",
        aspectratio=dict(x=1, y=1, z=0.5),
        camera=dict(
            eye=dict(x=0, y=2.5, z=0.1),
            up=dict(x=0, y=0, z=1)
        )
    )
)

fig.show()

