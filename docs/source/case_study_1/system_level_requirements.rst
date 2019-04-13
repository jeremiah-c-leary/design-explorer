*************************
System Level Requirements
*************************

=====  ====================
UID    Requirement/Heading
=====  ====================
---    Host Interface
001    The FPGA **shall** provide a host interface to configure, control, and retrieve status of the FPGA.
002    The host interface **shall** run at 80 MHz.
003    The host interface **shall** have one clock, one data, and one chip select.
---    ADC
004    The FPGA **shall** allow SW to configure the external ADC.
005    The FPGA **shall** allow SW to configure a threshold for incoming ADC data.
006    The FPGA **shall** set the yellow LED if the programmable threshold is exceeded.
---    Input Discretes
007    The FPGA **shall** reset all registers when the RESET input is asserted.
008    The FPGA **shall** allow SW to sample the input discretes.
---    Output Discretes
009    The FPGA **shall** allow SW to drive the output discretes.
010    The FPGA **shall** allow SW to read the value of the output discretes.
---    LEDs
011    The FPGA **shall** toggle the green LED when released from reset to indicate the FPGA is running.
---    Temperature Monitoring
012    The FPGA **shall** monitor an external temperature monitor.
---    External Switch
013    The FPGA **shall** disable the switch if the temperature exceeds a SW configurable value.
014    The FPGA **shall** set the red LED if the temperature exceeds a SW configurable value.
---    Clock Generator
015    The FPGA will receive a 40 MHz clock input.
=====  ====================
