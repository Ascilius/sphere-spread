from ursina import *
import math

def generate_sphere_grid(radius=0.5, lat_lines=6, lon_lines=12, segments=64):
    vertices = []

    # Latitude circles (horizontal rings)
    for i in range(1, lat_lines):  # skip poles
        lat = math.pi * (i / lat_lines - 0.5)  # -90° to 90°
        y = radius * math.sin(lat)
        r = radius * math.cos(lat)
        ring = []
        for j in range(segments + 1):
            theta = 2 * math.pi * j / segments
            x = r * math.cos(theta)
            z = r * math.sin(theta)
            ring.append(Vec3(x, y, z))
        for j in range(segments):
            vertices += [ring[j], ring[j + 1]]

    # Longitude circles (vertical rings, like meridians)
    for i in range(lon_lines):
        lon = 2 * math.pi * i / lon_lines
        ring = []
        for j in range(segments + 1):
            phi = math.pi * j / segments - math.pi / 2  # -90° to 90°
            x = radius * math.cos(phi) * math.cos(lon)
            y = radius * math.sin(phi)
            z = radius * math.cos(phi) * math.sin(lon)
            ring.append(Vec3(x, y, z))
        for j in range(segments):
            vertices += [ring[j], ring[j + 1]]

    return vertices

app = Ursina()

sphere = Entity(model = 'sphere', color = color.white33, collider = 'sphere', scale = 2)

grid_vertices = generate_sphere_grid(radius=0.501, lat_lines=6, lon_lines=12)
# radius slightly larger than 0.5 to avoid z-fighting with the sphere surface

grid = Entity(
    parent=sphere,
    model=Mesh(vertices=grid_vertices, mode='line', thickness=2),
    color = color.white
)

# The dot that will sit on the sphere's surface
dot = Entity(model = 'sphere', color = color.red, scale = 0.05, parent = sphere)
dot.enabled = False  # hide until first click

info_text = Text(text='', position=(-0.85, 0.45), scale=1.2)

EditorCamera()

def update():
    if held_keys['left mouse'] and mouse.hovered_entity == sphere:
        hit_point = mouse.world_point  # world-space point where the ray hit the sphere

        # Convert to the sphere's LOCAL space so it's independent of sphere position/rotation
        local_point = sphere.world_position_to_local(hit_point) if hasattr(sphere, 'world_position_to_local') else (hit_point - sphere.world_position)

        # Normalize to get a point on a unit sphere (removes scale)
        local_point = local_point.normalized()

        # Move the dot to sit exactly on the surface (in local coords, radius = 0.5 for Ursina's default sphere)
        dot.position = local_point * 0.5
        dot.enabled = True

        # --- Convert to latitude/longitude ---
        lat = math.degrees(math.asin(local_point.y))
        lon = math.degrees(math.atan2(local_point.z, local_point.x))

        info_text.text = f'Lat: {lat:.1f}°  Lon: {lon:.1f}°'

app.run()