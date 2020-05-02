# Summary


## Location [Details](coordinates/20200502location.md)

|      | Latitute   | Longitude   | Elevation (m) |
|------|------------|-------------|---------------|
| 10-m | 45.9555431 | -78.0701136 | 229           |
| 46-m | 45.9554015 | -78.0727995 | 245           |

**Separation:** 208 m.


## Gain [Details](FirstRunSimulation/20200502simulation.md)

The peak gain **on-axis is 32 dB** moving off-axis, gain falls to **5 dB or lower at 20 deg**.

![E and H gain slices](FirstRunSimulation/First.png)


## Calibration signal source [Details](SignalSource/signalSource.md)

If hanging something to the 46-m antenna doesn't work,
we can get a small drone with ~150 grams of payload.
I can think on two fast solutions a small signal generator
with an Arduino to switch the frequency every few seconds automatically and a known white source.
* Signal generator + control Arduino: 26 grams.
* Noise source + up converter: 43 grams
    Several parts can be cut to make it lighter.
* Supply: ~100 grams if going for the easy solution (AA batteries).

Using a small signal source allows to use small drones below the
250 grams limit to registering a drone.


## Tasks to do:
- Improve the model adding the ground plane behind the feed.
- Run the simulation with different feed misalignments.
- Assembly light weight signal sources for calibration.
