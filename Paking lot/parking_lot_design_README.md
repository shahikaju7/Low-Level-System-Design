# Parking Lot System Design

## Purpose
Design a parking lot system that supports parking and exiting vehicles while tracking spot availability, issuing tickets, and calculating fees.

## Functional Requirements
- Support multiple vehicle types: `CAR`, `BIKE`, and `TRUCK`.
- Maintain parking spots by size: `SMALL`, `MEDIUM`, `LARGE`.
- Assign vehicles to appropriately sized available spots.
- Issue a ticket when a vehicle is parked.
- Close the ticket and calculate fees when a vehicle exits.
- Track active tickets and free spot counts across floors.
- Handle a full parking lot condition gracefully.

## Non-Functional Requirements
- Use a singleton `Parkinglot` so only one instance manages the lot.
- Keep the design extensible for additional fee strategies.
- Maintain clear separation of responsibilities between classes.
- Keep parking logic simple and easy to extend.




