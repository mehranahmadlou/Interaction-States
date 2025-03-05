clear
dq = daq("ni");
dq.Rate = 1000;
ch_a0=addinput(dq,"NIDAQ_run","ai0","Voltage");
start(dq,"NumScans",10*dq.Rate);
pause(10)
scanData = read(dq,"all");
run_data = scanData.NIDAQ_run_ai0; 
plot(run_data)