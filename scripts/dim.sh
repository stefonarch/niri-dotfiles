#!/bin/bash

# Files to store state
BRIGHTNESS_FILE="$HOME/.brightness_level"
DIRECTION_FILE="$HOME/.brightness_direction"

# Initialize if files don't exist
if [ ! -f "$BRIGHTNESS_FILE" ]; then
    echo 100 > "$BRIGHTNESS_FILE"
fi

if [ ! -f "$DIRECTION_FILE" ]; then
    echo "down" > "$DIRECTION_FILE"
fi

BRIGHTNESS=$(cat "$BRIGHTNESS_FILE")
DIRECTION=$(cat "$DIRECTION_FILE")
STEP=20

# Adjust brightness based on direction
if [ "$DIRECTION" = "down" ]; then
    NEW_BRIGHTNESS=$((BRIGHTNESS - STEP))
    if [ "$NEW_BRIGHTNESS" -le 0 ]; then
        NEW_BRIGHTNESS=0
        echo "up" > "$DIRECTION_FILE"
    fi
else
    NEW_BRIGHTNESS=$((BRIGHTNESS + STEP))
    if [ "$NEW_BRIGHTNESS" -ge 100 ]; then
        NEW_BRIGHTNESS=100
        echo "down" > "$DIRECTION_FILE"
    fi
fi

# Apply new brightness
ddcutil setvcp 10 $1 "$NEW_BRIGHTNESS"

# Save new value
echo "$NEW_BRIGHTNESS" > "$BRIGHTNESS_FILE"

echo "Brightness set to $NEW_BRIGHTNESS ($DIRECTION)"
