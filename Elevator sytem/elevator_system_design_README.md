# Elevator System Design

## Purpose
Design a multi-elevator system that handles elevator requests from multiple floors, assigns elevators efficiently, and enforces capacity and door safety rules.

## Core Requirements
- Support multiple elevators and multiple floors.
- Allow users to request an elevator from any floor using UP or DOWN buttons.
- Each elevator can move up, move down, or remain idle.
- Assign the most suitable elevator to each request.
- Enforce a maximum weight capacity for each elevator.
- Open and close doors when the elevator reaches the requested floor.

## Constraints
- An elevator can only move one floor at a time.
- Prefer an elevator already moving in the same direction as the request.
- Use an idle elevator if no moving elevator is suitable.
- Doors can only open when the elevator is fully stopped.
- A file or folder must have a unique name within the same parent folder. (Note: This constraint is not about elevators; it belongs to file storage design.)

## Safety Rules
- Doors may only open when the elevator is stopped.
- An elevator must never exceed its weight capacity.
- If weight is over capacity, it should reject further boarding until weight is reduced.

## Possible Extensions
- Add support for destination buttons inside the elevator.
- Add priority handling for emergency requests.
- Add load balancing across multiple elevator banks.
- Add scheduled maintenance or out-of-service mode for elevators.
