# Smart Home Controller

This project simulates the control of a smart home system with multiple components (e.g., air conditioners, smart lights) using the Composite Design Pattern. It demonstrates how individual devices, rooms, floors, and entire houses can be controlled in a hierarchical manner.

## Structure

- **SmartComponent**: Common interface for all smart devices (e.g., air conditioners, lights).
- **AirConditioner**: Implementation of a smart air conditioner.
- **SmartLight**: Implementation of a smart light.
- **CompositeSmartComponent**: Composite class to group multiple smart components (e.g., multiple devices in a room, rooms in a floor).
- **SmartHomeController**: Main controller for demonstrating the operation of individual and composite devices.

## Requirements

- Python 3.x
- No external libraries are required

## Usage

1. **Create Individual Devices**: You can create individual devices like `AirConditioner` or `SmartLight`.
2. **Create Rooms**: Group devices into rooms using the `CompositeSmartComponent` class.
3. **Create Floors**: Group rooms into floors.
4. **Create Houses**: Group floors into houses.
5. **Control Devices**: Turn on/off all devices in the house, floor, or room.

### Example Usage

```python
from air_conditioner import AirConditioner
from smart_light import SmartLight
from composite_smart_component import CompositeSmartComponent

# Create individual devices
air_conditioner = AirConditioner()
smart_light = SmartLight()

# Create a room and add devices
room1 = CompositeSmartComponent()
room1.add_component(air_conditioner)
room1.add_component(smart_light)

# Create a floor and add rooms
floor = CompositeSmartComponent()
floor.add_component(room1)

# Create the house and add floors
house = CompositeSmartComponent()
house.add_component(floor)

# Control the entire house
print("Turning ON all devices in the house:")
house.turn_on()

print("\nTurning OFF all devices in the house:")
house.turn_off()
```
