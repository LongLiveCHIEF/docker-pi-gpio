# GPIO experiments in docker with gpio character device

tests need to be run with `-i` flag, in order to hold open the fd line
for the gpio character device. Once process exits, the line reverts
to it's unused state.

Example: 
`python -i tests/gpio.py`