# Analysis of video streaming performance:

## Tools:
- Selenium and chromedriver
- Python

### 2K Resolution:
- Buffer health increases sharply with network speed and plateaus after reaching a certain threshold.
- At lower speeds, buffer health is below the 5-second mark, which is inadequate.
- The plots indicate that to maintain a buffer health conducive to smooth streaming at 2K resolution, a higher network speed is necessary, ideally above 25 Mbps.

### 4K Resolution:
- The required network speed for adequate buffer health is even higher than for 2K, with buffer health becoming acceptable only at speeds above 40 Mbps.
- The curve suggests that for premium resolutions like 4K, high-speed and stable network connections are essential to prevent buffering.

### 360p Resolution:
- Buffer health is consistently high across all tested network speeds, rarely dropping near the 5-second threshold.
- This resolution is highly resilient to network speed changes, making it suitable for very low bandwidth environments.

### 480p Resolution:
- Similar to 360p, 480p also shows high buffer health across the spectrum of network speeds.
- It offers a middle ground between high accessibility and acceptable visual quality, making it a safe choice for users with limited internet speeds.

### 720p Resolution:
- 720p resolution maintains good buffer health even at moderate network speeds.
- It provides a balance between quality and performance, ensuring a better viewing experience without demanding very high network speeds.

### 1080p Resolution:
- Full HD content (1080p) shows that acceptable buffer health can be maintained even at lower network speeds compared to 2K and 4K resolutions.
- This suggests that 1080p streaming is more accessible to users with average network speeds while still providing high-definition content.

### General Observations:
- As the resolution increases, the network speed required to maintain good buffer health also increases.
- Lower resolutions like 360p and 480p ensure a smooth streaming experience across all network speeds, while higher resolutions are more susceptible to network variability.
- A buffer health of 5 seconds is the minimum required to avoid buffering issues, but for higher resolutions, a larger buffer is necessary to account for potential fluctuations in network speed.
