#Arduino Guide
> #Setup
> You will need to set up a 4.7k pull up resistor between 3.3 and the signal line. After doing this,
> define the pin used to connect the Onewire bus
```c 
  #define ONE_WIRE_BUS 12 // set this to the Arduino pin #
```
> After flashing the onboard LED should blink on and off for ~1 seconds to display it initialized.
> After that, it will blink every poll of the device(s).

## Note on parasite power
> As per the Dallas notes: parasite power will reduce the performance of conversion, so using it is not advisable.
> Since this code active polls for new devices, it can have a huge detriment to getting real time stats.